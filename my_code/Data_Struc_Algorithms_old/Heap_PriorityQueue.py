a = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq
heapq.heapify(a)

print(a)

heapq.heappush(a, 4)

print(a)

minn = heapq.heappop(a)

print(a, minn)

# Heap Sort

def heapsort(arr):
    heapq.heapify(arr)
    n - len(arr)
    new_list = [0] * n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn