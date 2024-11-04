def average_number(N):
    count = 0
    total_sum = 0

    for i in range(N):
        total_sum += i
        count += 1
    
    return total_sum/count

from multiprocessing import Process, Array


def worker(start, end, result, index):
    total_sum = 0
    for i in range(start, end):
        total_sum += i
    result[index] = total_sum

def parallel_sum(N):

    results = Array("i", 2)

    p1 = Process(target = worker, args = (0, N // 2, results, 0))
    p2 = Process(target = worker, args = (N // 2, N, results, 1))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Sum", sum(results))



# Race Condition: Multiple threads accessing shared data unpredictably
# Data Race: Simulatenous read/write on shared data that leads to inconsistency

import threading

def increment():
    global counter
    for _ in range(1000):
        count += 1

def increment_with_lock():
    global counter
    for _ in range(1000):
        with threading.Lock():
            counter += 1


def run_threads():
    global counter
    counter = 0
    threads = [threading.Thread(target = increment_with_lock) for _ in range(10)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Counter with race condition", counter)

# Task Parallelism: Different tasks on the same data can run in parallel
# Pipeline Parallelism: Parallelize sequential stages in a pipeline (1-5) (6-10)


def sum_worker(N, results):
    sum_nums = 0
    for i in range(0, N):
        sum_nums += i

    results[0] = sum_nums


def count_worker(N, results):
    results[1] = N

def average_task_parallel(N):
    results = Array("i", 2)
    p1 = Process(target = sum_worker, args = (N, results))
    p2 = Process(target = count_worker, args = (N, results))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    average = results[0] / results[1]

    print("Average", average)

# Write a function that calculates the factorial of numbers concurrently using pipeline parallelism

def factorial_numbers(start, stop):
    product = 1

    for i in range(start, stop + 1):
        product *= i
    
    return product

def find_factorials(N):

    num_chunks = N // 5

    threads_list = [None] * num_chunks

    for i in num_chunks:
        threads_list.append(threading.Thread(target = ))

if __name__ == "__main__":
    # parallel_sum(10)
    average_task_parallel(100)



