def Fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# ---- Input Section ----
try:
    n = int(input("Enter a non-negative integer n: "))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        result = Fib(n)
        print(f"The {n}th Fibonacci number is: {result}")
except ValueError:
    print("Invalid input! Please enter an integer.")