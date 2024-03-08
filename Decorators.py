def add(a, b):
    return a + b


def double_result(func):
    def wrapper(a, b):
        result = func(a, b)
        return result * 2

    return wrapper


add = double_result(add)


result = add(2, 3)
print(result)

# _______________________________________________________________


# def greet(fx):
#     def mfx():
#         print("good morning")
#         fx()
#         print("Thanks for using this function")

#     return mfx


# @greet
# def hello():
#     print("hello world")


# def add(a, b):
#     return a + b


# hello()


# ____________________________________________________________________________


# def hello():
# print("hello")


# def decorator(func):
#     def wrapper():
#         print("hello world")
#         return func

#     return wrapper


# hello = decorator(hello)


# hello()
