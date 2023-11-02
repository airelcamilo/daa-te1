import random
"""
Airel Camilo Khairan
2106652581
"""

class GenerateDataset:
    @staticmethod
    def generate(status, N):
        if status == "sorted":
            return GenerateDataset.sorted(N)
        elif status == "random":
            return GenerateDataset.random(N)
        elif status == "reversed":
            return GenerateDataset.reversed(N)
        return []

    @staticmethod
    def sorted(N):
        return [i for i in range(1, N+1)]
    
    @staticmethod
    def random(N):
        random.seed(N)
        return [random.randint(1, N+1) for _ in range(N)]
    
    @staticmethod
    def reversed(N):
        return [i for i in range(N, 0, -1)]
    
if __name__ == '__main__':
    with open("dataset.txt", "w") as file:
        for N in [2**9, 2**13, 2**16]:
            for status in ["sorted", "random", "reversed"]:
                A = GenerateDataset.generate(status, N)
                file.write(' '.join([status, str(N)]))
                file.write(' \n')
                file.write(' '.join([str(i) for i in A]))
                file.write('\n')
            