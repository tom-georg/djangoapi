import multiprocessing

bind = "127.0.0.1:8007"
workers = multiprocessing.cpu_count() * 2 + 1

max_requests = 500
