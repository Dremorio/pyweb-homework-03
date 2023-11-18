import time
from multiprocessing import Pool, cpu_count


def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def factorize_list(numbers):
    return [factorize(number) for number in numbers]


def parallel_factorize_list(numbers):
    with Pool(cpu_count()) as pool:
        result = pool.map(factorize, numbers)
    return result


def execution_time(func, args):
    start_time = time.time()
    result = func(args)
    return result, time.time() - start_time


test_numbers = [128, 255, 99999, 10651060]

result_sync, time_sync = execution_time(factorize_list, test_numbers)
result_parallel, time_parallel = execution_time(parallel_factorize_list, test_numbers)

print("Синхронна версія:")
print("Результат:", result_sync)
print("Час виконання:", time_sync, "секунд")

print("\nПаралельна версія:")
print("Результат:", result_parallel)
print("Час виконання:", time_parallel, "секунд")
