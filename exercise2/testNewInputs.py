import sys
from timeit import timeit
import matplotlib.pyplot as plt
import json
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if high - low <= 15:
        insertion_sort(arr, low, high)
        return
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi - 1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    median = median_of_three(array, start, end)
    pivot = array[median]
    array[median], array[start] = array[start], array[median]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def median_of_three(array, start, end):
    mid = (start + end) // 2
    if array[start] > array[mid]:
        array[start], array[mid] = array[mid], array[start]
    if array[start] > array[end]:
        array[start], array[end] = array[end], array[start]
    if array[mid] > array[end]:
        array[mid], array[end] = array[end], array[mid]
    return mid

def insertion_sort(array, start, end):
    for i in range(start + 1, end + 1):
        key = array[i]
        j = i - 1
        while j >= start and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

with open("ex2.json", "r") as file:
    inputs = json.load(file)
with open("ex2.5.json","r") as file:
    newInputs = json.load(file)
timing_results = []
timing_results_new = []
lengths = []
for arr in inputs:
    lengths.append(len(arr))
    timing_results.append(timeit(lambda:func1(arr, 0, len(arr) - 1),number=1))

for arr in newInputs:
    timing_results_new.append(timeit(lambda:func1(arr, 0, len(arr) - 1),number=1))

plt.plot(lengths,timing_results,label="Old data")
plt.plot(lengths,timing_results_new,label="New data")
plt.legend()
plt.xticks(lengths)
plt.xlabel("Number of items in input")
plt.ylabel("Time (seconds)")
plt.title("QuickSort Timing Results")
plt.show()
