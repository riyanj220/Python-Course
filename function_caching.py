from functools import lru_cache
import time


# @lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(5)
#     return n * 5


# print(fx(2))
# print("done for 2")
# print(fx(4))
# print("done for 4")
# print(fx(6))
# print("done for 6")


# print(fx(2))
# print("done for 2")
# print(fx(4))
# print("done for 4")
# print(fx(61))
# print("done for 6")
# ______________________________________________________________________


# @lru_cache(maxsize=None)
def fibonacci(n):
    if n < 3:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(60))
print(fibonacci(60))
