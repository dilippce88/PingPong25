def odd_even_sort(arr):
    n = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        # Odd indexed pass
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        # Even indexed pass
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

    return arr

# Take user input
try:
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, user_input.strip().split()))
    
    if not arr:
        print("Empty list provided.")
    else:
        sorted_arr = odd_even_sort(arr)
        print("Sorted list:", sorted_arr)

except ValueError:
    print("Invalid input. Please enter integers only.")
