import time


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


a = [5, 4, 3, 2, 1]
tic = time.perf_counter()
b = quicksort(a)
toc = time.perf_counter()

print(toc-tic)
