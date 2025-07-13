def find_smallest_element(arr):
    if not arr:
        return None
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

# Take user input
try:
    user_input = input("Enter elements of the array separated by spaces: ")
    array = list(map(int, user_input.strip().split()))
    if not array:
        print("The array is empty.")
    else:
        smallest = find_smallest_element(array)
        print(f"The smallest element in the array is: {smallest}")
except ValueError:
    print("Invalid input. Please enter integers only.")