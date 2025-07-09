def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Take input
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for _ in range(n):
    element = int(input())
    arr.append(element)

# Sort the array before binary search
arr.sort()
print("Sorted array:", arr)

target = int(input("Enter the element to search: "))

# Perform binary search
index = binary_search(arr, target)

# Output the result
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")