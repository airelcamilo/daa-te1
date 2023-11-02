from memory_profiler import memory_usage
from generate_dataset import *
import time
"""
Airel Camilo Khairan
2106652581
"""

class HeapSort:
    @staticmethod
    def max_heapify(A, n, i):
        left = 2*i + 1
        right = 2*i + 2
        max = i
        if left < n and A[left] > A[i]:
            max = left
        if right < n and A[right] > A[max]:
            max = right

        if max != i:
            A[i], A[max] = A[max], A[i]
            HeapSort.max_heapify(A, n, max)

    @staticmethod
    def build_max_heap(A):
        last_non_leaf_index = (len(A)-2)//2
        for index in range(last_non_leaf_index, -1, -1):
            HeapSort.max_heapify(A, len(A), index)

    @staticmethod
    def heap_sort(A):
        HeapSort.build_max_heap(A)
        for index in range(len(A)-1, 0, -1):
            A[0], A[index] = A[index], A[0]
            HeapSort.max_heapify(A, index, 0)

if __name__ == '__main__':
    with open("dataset.txt", "r") as file:
        for _ in range(9):
            status, N, _ = file.readline().split(" ")
            A = [int(num) for num in file.readline().split(" ")]
            memory_before = memory_usage()[0]
            start_time = time.perf_counter()

            HeapSort.heap_sort(A)

            total_runtime = time.perf_counter() - start_time
            memory_used = memory_usage()[0] - memory_before
            
            print(f"Status {status} | Ukuran {N}")
            print(f"Total runtime: {(total_runtime * 1000):.4f}ms")
            print(f"Memory usage : {(memory_used * 1024):.4f}KiB\n")