import threading

# Merge function
def merge(left, right):
    result = []
    i = j = 0

    # Merge the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Merge sort using threads
def threaded_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]

    left_sorted = []
    right_sorted = []

    # Create threads for left and right halves
    def sort_left():
        nonlocal left_sorted
        left_sorted = threaded_merge_sort(left_part)

    def sort_right():
        nonlocal right_sorted
        right_sorted = threaded_merge_sort(right_part)

    left_thread = threading.Thread(target=sort_left)
    right_thread = threading.Thread(target=sort_right)

    left_thread.start()
    right_thread.start()

    # Wait for both threads to complete
    left_thread.join()
    right_thread.join()

    return merge(left_sorted, right_sorted)

# ---------- Input Section ----------
n = int(input("Enter number of elements: "))
arr = []

print("Enter the elements:")
for _ in range(n):
    element = int(input())
    arr.append(element)

# ---------- Sort and Output ----------
sorted_arr = threaded_merge_sort(arr)
print("Sorted array:", sorted_arr)