import os

bind = "0.0.0.0:{}".format(os.getenv("PORT", "80"))
workers = 5
