def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("factorial of 3 is :", factorial(3))


# +++++++++++++++++++++++++++++++++++++++++++++++
def sum_of_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural(n - 1)


print(sum_of_natural(5))


# +++++++++++++++++++++++++++++++++++++++++++++++++
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
