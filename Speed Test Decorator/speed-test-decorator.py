import time

def speed_test(fn):
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"{fn.__name__} started...")
        
        result = fn(*args, **kwargs)
        
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"{fn.__name__} finished in {run_time:.4f} seconds")
        
        return result
    return inner

@speed_test
def sum_gen():
    # Generator kullanarak 0'dan 99,999,999'a kadar olan sayıları toplar
    return sum(x for x in range(100_000_000))

@speed_test
def sum_list():
    # Liste kullanarak 0'dan 99,999,999'a kadar olan sayıları toplar
    return sum([x for x in range(100_000_000)])

print(f"Result of sum_gen: {sum_gen()}")
print(f"Result of sum_list: {sum_list()}")
