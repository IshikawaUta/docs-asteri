import os
from flask import Flask, render_template, abort, request, jsonify
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension

from werkzeug.middleware.proxy_fix import ProxyFix
from flask_compress import Compress

app = Flask(__name__)
Compress(app)
# Force HTTPS in url_for and other dynamic links
app.config['PREFERRED_URL_SCHEME'] = 'https'
# Fix for HTTPS behind proxy (Railway, Cloudflare, etc.)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

@app.before_request
def redirect_www():
    """Redirect www to non-www for canonical URL stability."""
    from flask import redirect
    host = request.host.lower()
    if host.startswith('www.'):
        new_host = host[4:]
        url = request.url.replace(request.host, new_host, 1)
        return redirect(url, code=301)

@app.after_request
def add_security_headers(response):
    """Add security headers to every response."""
    # HSTS: Force HTTPS for 1 year
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
    # Additional Security Headers
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# Configuration
CONTENT_DIR = os.path.join(os.path.dirname(__file__), 'content')

# Sidebar Structure (File Tree style)
SIDEBAR = [
    {'title': 'Introduction to Asteri', 'id': 'introduction', 'icon': 'info'},
    {'title': 'Installation Guide', 'id': 'installation', 'icon': 'download'},
    {'title': 'Quick Start Guide', 'id': 'getting-started', 'icon': 'play'},
    {'title': 'Production Deployment', 'id': 'deployment', 'icon': 'server'},
    {'title': 'Mastering Worker Models', 'id': 'workers', 'icon': 'users'},
    {'title': 'CLI Mastery Reference', 'id': 'cli-reference', 'icon': 'terminal'},
    {'title': 'Advanced Configuration', 'id': 'configuration', 'icon': 'settings'},
    {'title': 'Status Dashboard', 'id': 'dashboard', 'icon': 'activity'},
    {'title': 'Release History', 'id': 'release-history', 'icon': 'history'},
    {'title': 'About the Developer', 'id': 'developer', 'icon': 'user'},
    {'title': 'License', 'id': 'license', 'icon': 'file-shield'},
]

def render_markdown(filename):
    filepath = os.path.join(CONTENT_DIR, f"{filename}.md")
    if not os.path.exists(filepath):
        return None
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    md = markdown.Markdown(extensions=[
        'extra',
        FencedCodeExtension(),
        CodeHiliteExtension(css_class='highlight', linenums=True),
        TableExtension(),
        TocExtension(baselevel=1, marker=None) # marker=None to prevent automatic injection
    ])
    html = md.convert(content)
    
    # Post-process HTML to add rel="noopener noreferrer" to external links
    import re
    html = re.sub(r'<a\s+(?![^>]*rel=)([^>]*href="https?://[^"]+"[^>]*)>', 
                  r'<a \1 rel="noopener noreferrer" target="_blank">', html)
    
    return html, md.toc

@app.route('/')
def index():
    return doc('introduction')

@app.route('/docs/<doc_id>')
def doc(doc_id):
    content_html, toc_html = render_markdown(doc_id)
    if content_html is None:
        abort(404)
    
    # Next/Prev logic
    current_index = next((i for i, item in enumerate(SIDEBAR) if item['id'] == doc_id), -1)
    prev_page = SIDEBAR[current_index - 1] if current_index > 0 else None
    next_page = SIDEBAR[current_index + 1] if current_index < len(SIDEBAR) - 1 else None
    
    # File metadata (Last Updated)
    import datetime
    filepath = os.path.join(CONTENT_DIR, f"{doc_id}.md")
    mtime = os.path.getmtime(filepath)
    last_updated = datetime.datetime.fromtimestamp(mtime).strftime('%b %d, %Y')
    
    current_page = SIDEBAR[current_index] if current_index != -1 else None
    
    return render_template('index.html', 
                           content=content_html, 
                           toc=toc_html,
                           sidebar=SIDEBAR, 
                           current_id=doc_id,
                           current_page=current_page,
                           prev_page=prev_page,
                           next_page=next_page,
                           last_updated=last_updated,
                           canonical_url=request.base_url.replace('http://', 'https://'))

@app.route('/api/search')
def search():
    import re
    query = request.args.get('q', '').lower()
    if not query or len(query) < 2:
        return jsonify([])
    
    results = []
    for item in SIDEBAR:
        content_html, _ = render_markdown(item['id'])
        # Strip HTML tags for searching
        text_content = re.sub('<[^<]+?>', '', content_html)
        
        if query in item['title'].lower() or query in text_content.lower():
            # Find snippet
            snippet = ""
            idx = text_content.lower().find(query)
            if idx != -1:
                start = max(0, idx - 40)
                end = min(len(text_content), idx + 60)
                snippet = "..." + text_content[start:end].strip() + "..."
            
            results.append({
                'title': item['title'],
                'id': item['id'],
                'snippet': snippet
            })
    
    return jsonify(results)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', 
                           content="<h1>404 - Page Not Found</h1><p>The documentation you are looking for does not exist.</p>", 
                           sidebar=SIDEBAR, 
                           current_id=None), 404

@app.route('/sitemap.xml')
def sitemap():
    from flask import make_response
    import datetime
    
    root_url = f"https://{request.host}/"
    pages = []
    # Add root
    pages.append({
        "loc": root_url,
        "lastmod": datetime.datetime.now().strftime("%Y-%m-%d"),
        "priority": "1.0"
    })
    
    # Add all docs
    for item in SIDEBAR:
        pages.append({
            "loc": f"{root_url}docs/{item['id']}",
            "lastmod": datetime.datetime.now().strftime("%Y-%m-%d"),
            "priority": "0.8"
        })
        
    sitemap_xml = render_template('sitemap.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/llms.txt')
def llms():
    from flask import Response
    content = render_template('llms.txt')
    return Response(content, mimetype='text/markdown')

@app.route('/robots.txt')
def robots():
    from flask import Response
    root_url = f"https://{request.host}/"
    content = f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {root_url}sitemap.xml"
    return Response(content, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=5000)