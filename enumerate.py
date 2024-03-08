marks = [12, 14, 15, 16, 13, 98, 67]
# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("riyan")
#     index += 1


for index, mark in enumerate(marks, start=1):
    print(mark)
    if index == 3:
        print("riyan")

# for value, value in enumerate(marks):
#     print(f"Value {value}: Value {value}")
