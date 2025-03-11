import time
from statistics import mean

def time_function(repetitions=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            execution_times = []
            for _ in range(repetitions):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_times.append(end_time - start_time)
            avg_time = mean(execution_times)
            print(f"Avg. execution time over {repetitions} repetitions: {avg_time} seconds")
            return avg_time 
        return wrapper
    return decorator



