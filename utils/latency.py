import time

def measure_latency(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        latency = time.perf_counter() - start
        return result, latency
    return wrapper