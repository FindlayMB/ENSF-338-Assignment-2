import sys
import json
from timeit import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("ex2.json", "r") as file:
    inputs = json.load(file)

timing_results = []

timing_results = []
lengths = []
for arr in inputs:
    lengths.append(len(arr))
    timing_results.append(timeit(lambda:func1(arr, 0, len(arr) - 1),number=1))


plt.plot(lengths,timing_results,label="Original Version")
plt.legend()
plt.xticks(lengths)
plt.xlabel("Number of items in input")
plt.ylabel("Time (seconds)")
plt.title("QuickSort Timing Results")
plt.show()
