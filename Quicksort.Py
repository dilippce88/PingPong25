def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)


n = int(input("Enter number of elements: "))
arr = []

print("Enter the elements:")
for _ in range(n):
    element = int(input())
    arr.append(element)

sorted_arr = quicksort(arr)

print("Sorted array:", sorted_arr)