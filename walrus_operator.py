# a = 5
# b = 5
# print(a + b)

# ab walrus operator ki madad se ik hi line me hogya kaam

# print((a := 5) + (b := 5))

# ______________________________________________________
# num = [1, 2, 3, 4, 5]
# while n := len(num) > 0:
#     print(num.pop())

# _______________________________________________________________

foods = list()
while True:
    food = input("What food do you like? ")
    foods.append(food)
    if food == "quit":
        break
print(foods)

# ab dekho yeh walrus operator ki madad se 7 lines ka code 4 line me hogya hy
foods = list()
while (food := input("what food you like? ")) != "quit":
    foods.append(food)
print(foods)
