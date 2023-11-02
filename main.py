from memory_profiler import memory_usage
from randomized_shell_sort import *
from max_heap_sort import *
"""
Airel Camilo Khairan
2106652581
"""

if __name__ == '__main__':
    with open("dataset.txt", "r") as file:
        for _ in range(9):
            status, N, _ = file.readline().split(" ")
            A = [int(num) for num in file.readline().split(" ")]
            B = A.copy()
            
            memory_before = memory_usage()[0]
            start_time = time.perf_counter()

            ShellSort.randomized_shell_sort(A)

            total_runtime = time.perf_counter() - start_time
            memory_used = memory_usage()[0] - memory_before
            
            print(f"Status {status} | Ukuran {N}")
            print(f"-- Randomized Shell Sort --")
            print(f"Total runtime: {(total_runtime * 1000):.4f}ms")
            print(f"Memory usage : {(memory_used * 1024):.4f}KiB\n")

            memory_before = memory_usage()[0]
            start_time = time.perf_counter()

            HeapSort.heap_sort(B)

            total_runtime = time.perf_counter() - start_time
            memory_used = memory_usage()[0] - memory_before
            
            print(f"------ Max Heap Sort ------")
            print(f"Total runtime: {(total_runtime * 1000):.4f}ms")
            print(f"Memory usage : {(memory_used * 1024):.4f}KiB\n")
            assert A == B