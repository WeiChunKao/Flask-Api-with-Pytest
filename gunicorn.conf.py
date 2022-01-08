import multiprocessing
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
bind = ':5000'
timeout = 60
keepalive = 60
