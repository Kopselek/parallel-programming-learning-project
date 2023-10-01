from joblib import Parallel, delayed
import math
import time
import matplotlib.pyplot as plt

selected_number = 100


def calculate_expression(x):
    return math.pow(x, 1 / 3) + 2 * x + 4


def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


def calculate_expression_add(x):
    return x + selected_number


def calculate_expression_subtraction(x):
    return x - selected_number


def calculate_expression_multiplication(x):
    return x * selected_number


def calculate_expression_division(x):
    return x / selected_number


def calculate_expression_square(x):
    return math.pow(x, 2)


def calculate_expression_power(x):
    return math.sqrt(x)


def measure_time_sequential(func, n):
    start = time.time()
    for i in range(n):
        result = func(i)
    end = time.time()
    return end - start


def measure_time_threads(func, n, prefer="processes"):
    start = time.time()
    delayed_func = [delayed(func)(i) for i in range(n)]
    parallel_pool = Parallel(n_jobs=-1, prefer=prefer)
    parallel_pool(delayed_func)
    end = time.time()
    return end - start



operation_functions = [
    calculate_expression_add,
    calculate_expression_subtraction,
    calculate_expression_multiplication,
    calculate_expression_division,
    calculate_expression_square,
    calculate_expression_power
]

n = 50000
for operation_func in operation_functions:
    sequential_time = measure_time_sequential(operation_func, n)
    parallel_threads_time = measure_time_threads(operation_func, n)
    parallel_processes_time = measure_time_threads(operation_func, n, "threads")

    print(f"Operation: {operation_func.__name__}")
    print(f"n={n}:")
    print(f"Sequential: {sequential_time:.6f} seconds")
    print(f"Parallel (Threads): {parallel_threads_time:.6f} seconds")
    print(f"Parallel (Processes): {parallel_processes_time:.6f} seconds")
    print("-" * 40)

sequential_times = []
parallel_threads_times = []
parallel_processes_times = []

n_values = [10000, 25000, 50000, 100000, 500000]
for n in n_values:
    sequential_time = measure_time_sequential(operation_func, n)
    parallel_threads_time = measure_time_threads(operation_func, n)
    parallel_processes_time = measure_time_threads(operation_func, n, "threads")

    sequential_times.append(sequential_time)
    parallel_threads_times.append(parallel_threads_time)
    parallel_processes_times.append(parallel_processes_time)

labels = [str(n) for n in n_values]

plt.figure(figsize=(12, 6))
width = 0.2
x = range(len(labels))

plt.bar([i - width for i in x], sequential_times, width=width, label="Sequential", color='blue', alpha=0.7)
plt.bar(x, parallel_threads_times, width=width, label="Parallel (Threads)", color='green', alpha=0.7)
plt.bar([i + width for i in x], parallel_processes_times, width=width, label="Parallel (Processes)", color='orange',
        alpha=0.7)

plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Performance Comparison for Different n Values (calculate_expression)")
plt.xticks(x, labels)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
