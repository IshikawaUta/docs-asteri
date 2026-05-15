# 🛠️ Getting Started

Asteri includes several examples to get you started with different frameworks and protocols.

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
