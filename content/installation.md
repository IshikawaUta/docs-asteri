# 🚀 Installation & Deployment

Asteri is designed to be lightweight and easy to integrate into any environment, from local development to large-scale production clusters.

## Standard Installation

You can install Asteri directly from source for the latest features:

```bash
git clone https://github.com/IshikawaUta/asteri.git
cd asteri
pip install .
```

## Production Deployment

For production environments, we recommend running Asteri behind a reverse proxy like Nginx and managing the process with Systemd.

### 🛡️ Nginx Configuration

Nginx should handle SSL termination and static file serving, forwarding application requests to Asteri.

```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    
    location /static/ {
        alias /path/to/your/app/static/;
    }
}
```

### ⚙️ Systemd Service

Create a service file at `/etc/systemd/system/asteri.service`:

```ini
[Unit]
Description=Asteri Web Server
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/your/app
ExecStart=/usr/local/bin/asteri myapp:app -w 4 -k gthread -b 127.0.0.1:8000
Restart=always

[Install]
WantedBy=multi-user.target
```

## Dependencies

- **Python**: 3.8 or higher.
- **Watchdog**: Required for the `--reload` feature.
- **Gevent**: Required if using the `gevent` worker class.
- **Setproctitle**: Optional, used for professional process naming in `ps` or `top`.
