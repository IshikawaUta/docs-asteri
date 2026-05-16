# 🚢 Production Deployment Guide

Deploying Asteri in a production environment requires careful configuration to ensure maximum security, performance, and uptime. This guide outlines the best practices for hosting Asteri-powered applications.

## 🛡️ Reverse Proxy Architecture (Nginx)

Nginx should handle SSL termination and static file serving, forwarding application requests to Asteri. This improves performance and provides an additional layer of security.

```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Static file serving
    location /static/ {
        alias /path/to/your/app/static/;
        expires 30d;
        add_header Cache-Control "public, no-transform";
    }
}
```

## ⚙️ Process Management (Systemd)

Using Systemd ensures that Asteri starts automatically on boot and restarts if it crashes. Create a service file at `/etc/systemd/system/asteri.service`:

```ini
[Unit]
Description=Asteri Web Server
After=network.target

[Service]
# User and Group to run the workers under
User=www-data
Group=www-data
WorkingDirectory=/path/to/your/app
# Use the full path to the asteri executable
ExecStart=/usr/local/bin/asteri myapp:app \
    -w 4 \
    -k gthread \
    -b 127.0.0.1:8000 \
    --access-logfile /var/log/asteri/access.log \
    --error-logfile /var/log/asteri/error.log
Restart=always

[Install]
WantedBy=multi-user.target
```

### Managing the Service

```bash
# Reload systemd to recognize the new service
sudo systemctl daemon-reload

# Start and enable the service
sudo systemctl start asteri
sudo systemctl enable asteri

# Check status
sudo systemctl status asteri
```

## 🐳 Docker Deployment

You can also containerize your Asteri application.

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir .

EXPOSE 8000

CMD ["asteri", "myapp:app", "-w", "4", "-b", "0.0.0.0:8000"]
```
