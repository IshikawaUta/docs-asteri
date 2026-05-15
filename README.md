# 🌌 Asteri Documentation Website

A professional, high-performance documentation website for the **Asteri Web Server**, featuring a modern "Code Editor" theme, global search, and full mobile responsiveness.

![Asteri Docs Preview](static/images/favicon.png)

## ✨ Features

- **Code Editor Theme**: Premium dark-mode UI inspired by modern IDEs.
- **Global Search**: Instant search with text highlighting and auto-scrolling (Shortcut: `/`).
- **Dynamic Sidebar**: Collapsible file-explorer style navigation.
- **On-This-Page Navigation**: Sticky right-sidebar TOC for quick internal document jumps.
- **Mobile Optimized**: Responsive tables, fluid layouts, and a dedicated mobile sidebar overlay.
- **Developer First**: Automatic code block copy buttons and "Edit on GitHub" integration.
- **Markdown Driven**: Content is fully modular and written in pure Markdown.

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Styling**: Tailwind CSS (CDN) & Vanilla CSS
- **Markdown**: Python-Markdown (with Extra, CodeHilite, Fenced Code, and Tables extensions)
- **Icons**: Lucide Icons & FontAwesome
- **Syntax Highlighting**: Pygments (Monokai-like theme)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [Asteri Web Server](https://pypi.org/project/asteri/) (Optional, but recommended for serving)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/IshikawaUta/docs-asteri.git
   cd docs-asteri
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   # Using Flask Development Server
   python app.py
   
   # OR Using Asteri (Production Ready)
   asteri app:app -k gevent -w 4 -b 127.0.0.1:8000 --reload
   ```

## 📂 Project Structure

```text
├── app.py              # Flask application logic
├── content/            # Documentation Markdown files
├── static/
│   ├── css/            # Custom styles & Pygments CSS
│   └── images/         # Logo, favicon, and screenshots
└── templates/          # Jinja2 HTML templates
```

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
*Created by [IshikawaUta](https://github.com/IshikawaUta).*
