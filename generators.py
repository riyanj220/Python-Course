# def generator():
#     for i in range(11):
#         yield i


# gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# ________________________________________________________________
# def generate_squares(n):
#     for i in range(n):
#         yield i**2


# for square in generate_squares(6):
#     print(square)
# ________________________________________________________________


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fb = fibonacci()
for _ in range(10):
    print(next(fb))
