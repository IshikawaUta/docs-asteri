lucide.createIcons();

// Sidebar Toggle
const sidebar = document.getElementById('sidebar');
const toggleBtn = document.getElementById('sidebarToggle');
const overlay = document.getElementById('sidebarOverlay');
const closeBtn = document.getElementById('closeSidebar');

// Auto-collapse sidebar on mobile
if (window.innerWidth <= 768) {
    sidebar.classList.add('collapsed');
}

const toggleSidebar = () => {
    sidebar.classList.toggle('collapsed');
};

if (toggleBtn) toggleBtn.addEventListener('click', toggleSidebar);
if (overlay) overlay.addEventListener('click', toggleSidebar);
if (closeBtn) closeBtn.addEventListener('click', toggleSidebar);

// Keyboard Shortcut for Sidebar (Ctrl + B)
document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'b') {
        e.preventDefault();
        sidebar.classList.toggle('collapsed');
    }
});

// Collapsible Sidebar Groups
document.querySelectorAll('.group-header').forEach(header => {
    header.addEventListener('click', () => {
        const targetId = header.getAttribute('data-target');
        const content = document.getElementById(targetId);
        const chevron = header.querySelector('.chevron-icon');
        
        content.classList.toggle('hidden');
        chevron.classList.toggle('rotated');
    });
});

// Copy Code Feature
document.querySelectorAll('pre').forEach(pre => {
    // Wrap pre in a container
    const container = document.createElement('div');
    container.className = 'code-container mb-6';
    pre.parentNode.insertBefore(container, pre);
    container.appendChild(pre);

    // Create copy button
    const button = document.createElement('button');
    button.className = 'copy-button';
    button.innerHTML = '<i data-lucide="copy" class="w-4 h-4"></i>';
    container.appendChild(button);

    button.addEventListener('click', () => {
        const code = pre.innerText;
        navigator.clipboard.writeText(code).then(() => {
            button.classList.add('copied');
            button.innerHTML = '<i data-lucide="check" class="w-4 h-4"></i>';
            lucide.createIcons();
            
            setTimeout(() => {
                button.classList.remove('copied');
                button.innerHTML = '<i data-lucide="copy" class="w-4 h-4"></i>';
                lucide.createIcons();
            }, 2000);
        });
    });
});

// Search Functionality
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');

let searchTimeout;
if (searchInput) {
    searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        const query = e.target.value.trim();
        
        if (query.length < 2) {
            searchResults.classList.add('hidden');
            return;
        }

        searchTimeout = setTimeout(async () => {
            const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
            const data = await response.json();
            
            if (data.length > 0) {
                searchResults.innerHTML = data.map(result => `
                    <a href="/docs/${result.id}?highlight=${encodeURIComponent(query)}" class="block p-3 border-b border-gray-800 hover:bg-white/5 transition-colors">
                        <div class="text-blue-400 font-medium text-xs mb-1">${result.title}</div>
                        <div class="text-[10px] text-gray-400 line-clamp-2">${result.snippet}</div>
                    </a>
                `).join('');
                searchResults.classList.remove('hidden');
            } else {
                searchResults.innerHTML = '<div class="p-3 text-[10px] text-gray-500">No results found</div>';
                searchResults.classList.remove('hidden');
            }
        }, 300);
    });

    // Close search when clicking outside
    document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.classList.add('hidden');
        }
    });

    // Search Shortcut (/)
    document.addEventListener('keydown', (e) => {
        if (e.key === '/' && document.activeElement !== searchInput) {
            e.preventDefault();
            searchInput.focus();
        }
    });
}

// Search Highlighting
const urlParams = new URLSearchParams(window.location.search);
const searchHighlight = urlParams.get('highlight');
if (searchHighlight) {
    const contentArea = document.querySelector('.editor-content');
    
    // Safety: escape special regex characters and only match text outside of HTML tags
    const escapedQuery = searchHighlight.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const regex = new RegExp(`(<[^>]*>)|(${escapedQuery})`, 'gi');
    
    contentArea.innerHTML = contentArea.innerHTML.replace(regex, (match, p1, p2) => {
        if (p1) return p1; // It's an HTML tag, return it as is
        return `<span class="search-highlight">${p2}</span>`; // It's a text match, wrap it
    });
    
    // Scroll to first highlight
    const firstHighlight = document.querySelector('.search-highlight');
    if (firstHighlight) {
        firstHighlight.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

// Right Sidebar (TOC) ScrollSpy
const tocLinks = document.querySelectorAll('.right-sidebar .toc a');
const headings = Array.from(document.querySelectorAll('.editor-content h1, .editor-content h2, .editor-content h3'));
const mainContent = document.querySelector('main .overflow-y-auto');

if (tocLinks.length > 0 && headings.length > 0 && mainContent) {
    mainContent.addEventListener('scroll', () => {
        let current = "";
        const scrollPosition = mainContent.scrollTop + 100;

        headings.forEach(heading => {
            const headingTop = heading.offsetTop;
            if (scrollPosition >= headingTop) {
                current = heading.getAttribute('id');
            }
        });

        tocLinks.forEach(link => {
            link.classList.remove('active-toc');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active-toc');
            }
        });
    });
}

// Scroll to Top Logic
const scrollToTopBtn = document.getElementById('scrollToTop');
const contentArea = document.querySelector('main .overflow-y-auto');

if (contentArea && scrollToTopBtn) {
    contentArea.addEventListener('scroll', () => {
        if (contentArea.scrollTop > 300) {
            scrollToTopBtn.classList.remove('hidden');
        } else {
            scrollToTopBtn.classList.add('hidden');
        }
    });

    scrollToTopBtn.addEventListener('click', () => {
        contentArea.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Keyboard Shortcut (T or Home key)
    document.addEventListener('keydown', (e) => {
        // Only trigger if not typing in search input
        if (document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'TEXTAREA') {
            return;
        }

        if (e.key.toLowerCase() === 't' || e.key === 'Home') {
            e.preventDefault();
            contentArea.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
    });
}

lucide.createIcons();
