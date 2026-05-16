# 🚀 Installation Guide

Asteri is a lightweight, high-performance Python web server. Follow this guide to install Asteri on your system and start deploying your applications.

## Quick Install (PyPI)

The easiest way to get Asteri is directly from the Python Package Index (PyPI):

```bash
pip install asteri
```

## Source Installation

For developers who want the absolute latest features or wish to contribute, you can install Asteri from the GitHub repository:

```bash
git clone https://github.com/IshikawaUta/asteri.git
cd asteri
pip install .
```


## Dependencies

- **Python**: 3.8 or higher.
- **Watchdog**: Required for the `--reload` feature.
- **Gevent**: Required if using the `gevent` worker class.
- **Setproctitle**: Optional, used for professional process naming in `ps` or `top`.
