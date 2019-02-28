import os

bind = "0.0.0.0:{}".format(os.getenv("PORT", "8000"))
worker_class = "gevent"
worker_connections = 100
