def heapify(arr, n, i):
    largest = i      # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # See if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root again
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# ----------- Input Section -----------
try:
    user_input = input("Enter the elements to sort (space-separated): ")
    arr = list(map(int, user_input.strip().split()))

    heap_sort(arr)

    print("Sorted array:", arr)

except ValueError:
    print("Invalid input. Please enter space-separated integers.")