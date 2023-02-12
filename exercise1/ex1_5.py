
import timeit
import matplotlib.pyplot as plt


def optimized_fibonacci(num, memory = {0:0, 1:1}):
    if num not in memory:
        memory[num] =optimized_fibonacci(num-1, memory) + optimized_fibonacci(num-2, memory)
    return memory[num]

def original_fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return original_fibonacci(num-1) + original_fibonacci(num-2)

elapsedTimeOriginal = []
elapsedTimeOptimized = []
for i in range(36):
    timeOriginal = timeit.timeit(lambda: original_fibonacci(i), number=1)
    elapsedTimeOriginal.append(timeOriginal)
for i in range(36):
    memory = {}
    timeOptimized = timeit.timeit(lambda: optimized_fibonacci(i),number=1)
    elapsedTimeOptimized.append(timeOptimized)

plt.plot(elapsedTimeOriginal,label="Original Fibonacci")
plt.plot(elapsedTimeOptimized,label="Optimized Fibonacci")
plt.xlabel("nth Fibonacci Number Calculated")
plt.ylabel("Time (seconds)")
plt.xticks(range(36))
plt.yticks(range(6),minor=True)
plt.legend()
plt.show()
