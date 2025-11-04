import os

# Bind to 0.0.0.0 to allow external access
bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"

# Number of worker processes for handling requests
workers = int(os.environ.get('WEB_CONCURRENCY', 4))

# Whether to reload the server when code changes
reload = os.environ.get('FLASK_ENV') == 'development'

# Maximum number of requests a worker will process before restarting
max_requests = 1000

# Maximum amount of time (in seconds) a worker will work before being restarted
max_requests_jitter = 50

# Access log config
accesslog = '-'
errorlog = '-'