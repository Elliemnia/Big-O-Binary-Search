import math

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


if __name__=='__main__':
    n = 1000000
    arr = list(range(n))

# calculate the time complexity of binary search
    time_complexity = math.log2(n)

    print(f"The time complexity of binary search on an array of size {n} is O(log n) = {time_complexity}")