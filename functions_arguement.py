def average(*numbers):  # tuple create karega *
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average is :", sum / len(numbers))


average(5, 6, 4, 5, 6)


# =========================================
def name(**name):  # dictionary create karega **
    print("hello", name["fname"]), name["mname"], name["lname"]


name(mname="adafsadf", lname="afdfsa", fname="james")
