# try:
#     a = int(input("enter a number:"))
#     b = a / 2
#     print(b)
# except Exception as e:
#     print(f"Type error:{e}")
# print("ancd")


# ____________________________________________________________


# a = input("Enter a Number:")
# print(f"Multiplication table of {a} is:")

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")

# except Exception as e:
#     print(e)

# print("some imp lines of code")
# print("end of code")


# _________________________________________________________
def func1():
    try:
        l = [1, 23, 4, 5, 6]
        i = int(input("Enter index number:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0

    finally:
        print("it alwasy gets executes")


x = func1()
print(x)
