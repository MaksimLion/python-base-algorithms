import time


def time_checker(func):
    
    def wrapper(a, b):
        start_time = time.time()
        result = func(a, b)
        print(time.time() - start_time)
        return result

    return wrapper