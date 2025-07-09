def highest_product_of_three(nums):
    nums.sort()

    # Case 1: Product of three largest numbers
    max_product_1 = nums[-1] * nums[-2] * nums[-3]

    # Case 2: Product of two smallest (most negative) and the largest
    max_product_2 = nums[0] * nums[1] * nums[-1]

    return max(max_product_1, max_product_2)

# ----------- Input Section ------------
n = int(input("Enter number of elements: "))
arr = []

print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))

if n < 3:
    print("Need at least 3 numbers to find the highest product.")
else:
    result = highest_product_of_three(arr)
    print("Highest product of three numbers is:", result)