def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 30  # increase your input as your requirement
fib_series = [fibonacci(i) for i in range(1, n+1)]
print(fib_series)