from memory_profiler import memory_usage
from generate_dataset import *
import time
"""
Airel Camilo Khairan
2106652581
"""

class ShellSort:
    C = 1
    
    @staticmethod
    def exchange(A, i, j):
        A[i], A[j] = A[j], A[i]

    @staticmethod
    def compare_exchange(A, i, j):
        if ((i < j) and (A[i] > A[j])) or ((i > j) and A[i] < A[j]):
            ShellSort.exchange(A, i, j)

    @staticmethod
    def permute_random(A):
        for i in range(len(A)):
            ShellSort.exchange(A, i, random.randint(0, len(A) - 1 - i) + i)

    @staticmethod
    def compare_regions(A, s, t, offset):
        mate = [i for i in range(offset)]
        for _ in range(ShellSort.C):
            ShellSort.permute_random(mate)
            for i in range(offset):
                ShellSort.compare_exchange(A, s + i, t + mate[i])

    @staticmethod
    def randomized_shell_sort(A):
        random.seed(1)
        n = len(A)
        offset = n//2
        while offset > 0:
            # Compare-Exchange Up
            for i in range(0, n - offset, offset):
                ShellSort.compare_regions(A, i, i + offset, offset)
            # Compare-Exchange Down
            for i in range(n - offset, offset - 1, -offset):
                ShellSort.compare_regions(A, i - offset, i, offset)
            # Compare 3 hops up
            for i in range(0, n - 3*offset, offset):
                ShellSort.compare_regions(A, i, i + 3*offset, offset)
            # Compare 2 hops up
            for i in range(0, n - 2*offset, offset):
                ShellSort.compare_regions(A, i, i + 2*offset, offset)
            # Compare odd-even regions
            for i in range(0, n, 2*offset):
                ShellSort.compare_regions(A, i, i + offset, offset)
            # Compare even-odd regions
            for i in range(offset, n - offset, 2*offset):
                ShellSort.compare_regions(A, i, i + offset, offset)
            offset //= 2

if __name__ == '__main__':
    with open("dataset.txt", "r") as file:
        for _ in range(9):
            status, N, _ = file.readline().split(" ")
            A = [int(num) for num in file.readline().split(" ")]
            memory_before = memory_usage()[0]
            start_time = time.perf_counter()

            ShellSort.randomized_shell_sort(A)

            total_runtime = time.perf_counter() - start_time
            memory_used = memory_usage()[0] - memory_before
            
            print(f"Status {status} | Ukuran {N}")
            print(f"Total runtime: {(total_runtime * 1000):.4f}ms")
            print(f"Memory usage : {(memory_used * 1024):.4f}KiB\n")