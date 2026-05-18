# 🛠️ Quick Start Guide

Ready to experience high-performance Python serving? This guide will show you how to launch your first Asteri-powered application in seconds.

## Basic Usage

Run a standard WSGI application:
```bash
asteri myapp:app
```

Run with 4 workers and bind to multiple ports:
```bash
asteri myapp:app -w 4 -b 127.0.0.1:8000 -b 127.0.0.1:8001
```

## Running Examples

### Flask (WSGI)
Run with thread-based workers:
```bash
python3 -m asteri example_flask:app -k gthread -w 4 -b 127.0.0.1:8000
```

### FastAPI (ASGI)

Run with modern async workers:
```bash
python3 -m asteri example_fastapi:app -k asgi -w 4 -b 127.0.0.1:8000
```

### Production with Nginx (uWSGI)

Run Asteri in uWSGI mode (automatic detection) and use the provided `example_uwsgi_nginx.conf`:
```bash
python3 -m asteri example_wsgi:app -b 127.0.0.1:8000
```

### HTTP/3 (QUIC) — New in v2.2.2

Enable native HTTP/3 support with the `--http-protocols` flag:
```bash
python3 -m asteri example_fastapi:app -k asgi -w 4 --http-protocols h3 -b 127.0.0.1:8000
```

### Prometheus Metrics — New in v2.2.2

Asteri exposes a `/metrics` endpoint automatically with no extra configuration needed:
```bash
curl http://127.0.0.1:8000/metrics
```
