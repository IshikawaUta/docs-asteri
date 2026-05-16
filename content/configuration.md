# ⚙️ Advanced Configuration Guide

Asteri is designed for ultimate flexibility. Whether you prefer quick CLI flags, environment-specific variables, or professional Python-based configuration files, Asteri gives you total control over your server environment.

## Configuration Hierarchy

When settings are defined in multiple places, Asteri follows this priority (highest to lowest):

1. **Command Line Arguments** (overrides everything)
2. **Environment Variables**
3. **Configuration File**
4. **Default Values**

## The Configuration File

Using a Python configuration file is the most "professional" way to manage complex application settings. It allows for dynamic logic and clear organization.

## 📝 Comprehensive Example (`asteri.conf.py`)

```python
# Network Settings
bind = ["127.0.0.1:8000", "0.0.0.0:443"]
backlog = 2048

# Worker Settings
workers = 4
worker_class = "gthread"
threads = 4
worker_connections = 1000
timeout = 60
graceful_timeout = 30
keep_alive = 2
max_requests = 1000
max_requests_jitter = 50
preload = True

# Security Settings
certfile = "/etc/ssl/certs/asteri.crt"
keyfile = "/etc/ssl/private/asteri.key"
user = "asteri-user"
group = "asteri-group"

# Logging Settings
access_logfile = "/var/log/asteri/access.log"
error_logfile = "/var/log/asteri/error.log"
log_level = "info"
capture_output = True

# Process Settings
daemon = True
pid = "/run/asteri.pid"
name = "asteri-prod-app"
reload = False
```

## Running with Configuration

To start Asteri using a configuration file, use the `-c` or `--config` flag:

```bash
asteri myapp:app -c asteri.conf.py
```

## 💡 Tips for Config Files

- **Lists for Bindings**: Always use a list for the `bind` variable if you want to listen on multiple ports.
- **Python Logic**: Since the config file is a Python script, you can use logic to determine settings based on environment:
  ```python
  import os
  workers = os.cpu_count() * 2 + 1
  debug = os.getenv("DEBUG") == "True"
  log_level = "debug" if debug else "info"
  ```
