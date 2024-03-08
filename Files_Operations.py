# *****READING FROM FILES*****


# file = open("practice2.txt", "r")
# content = file.read() #read from  a file
# print(content)
# file.close()


# file = open("practice2.txt", "r")
# content = file.readline() #read a single line from file
# print(content)
# file.close()


# file = open("practice2.txt", "r")
# content = file.readlines()  # saari line parhay ga aur list of strings me dega output
# print(content)
# file.close()

# with open("practice2.txt") as f:
#     while True:
#         line = f.readline()
#         print(line)
#         if not line:
#             break

# ____________________________________________________________

# *****WRITING TO FILES*****


# file = open("practice2.txt", "w") #simple overwrite krdega jo pehle se likha hoga
# file.write("riyan is the don")
# file.close()

# _____________________________________________________________________


# convenient way to open file isme close krne ki zaroat ni rehti

# with open("practice2.txt", "a") as file:
#     file.write("\nok now i haved append") #ese ham append kr skty hy

# __________________________________________________________________


# agar hame specific line delete krna ho to ese kren ge


# text_to_delete = "Okk now i haved append"
# with open("practice2.txt", "r") as file:
#     lines = file.readlines()

# modified_lines = [line for line in lines if text_to_delete not in line]

# with open("practice2.txt", "w") as file:
#     file.writelines(modified_lines)

# _______________________________________________________________________


# with open("practice22.txt", "w") as file:
#     file.write("ok new file created and written in it") #agar write mode me kholo gy file ko aur file pehly se mojood ni huyi to wo create hojayegi

# _______________________________________________________________________

# with open("practice2.txt", "w") as file:
#     lines = ["line 1\n", "line 2\n", "line 3"]
#     file.writelines(lines) #agar aap lines apni text file me chupkana chhaty hy to krksyt hy iterable hy yeh


# miscellaneous wroking with files

# with open("practice.txt", "r") as file:
#     file.seek(
#         10
#     )  # iska mtlb aap apni marzi se byte jump kr ke whn se read waghera kar skty hay
#     data = file.read(5)  # ab ye 10 bytes aagey kar ke 5 bytes read krega
#     print(data)


# with open("practice.txt", "r") as file:
#     file.seek(5)


#     print(file.tell()) #ye aapko ye bataye ga ke seek kahan tk kia hua


# with open("practice.txt", "w") as file:
#     file.write("hello world")
#     file.truncate(
#         5
#     )  # ab hamne write to krdiya hy liken ham agar chahy to jo likh chuky uska byte ka size kam kar ke utna byte me jo aye wo dikha skty hy

# with open("practice.txt", "r") as file:
#     print(file.read())
