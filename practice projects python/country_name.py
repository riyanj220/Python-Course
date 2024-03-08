questions = [
    "What is the capital of Afghanistan?\n\n A.Bangul\n B.zagreb\n C.kabul\n",
    "what is the capital of Bangladesh?\n\n A.Moroni\n B.Dhaka\n C.Asmara\n",
    "what is the capital of China?\n\n A.Beijing\n B.Morocco\n C.Conakkry\n",
    "what is the capital of Germany?\n\n A.Majuro\n B.Malta\n C.Berlin\n",
]
answers = ["c", "b", "a", "c"]

for i in range(len(questions)):
    print(questions[i])

    user_answer = input("Enter Options:").strip().lower()
    if user_answer == answers[i]:
        print("Congragulations!\nAnswer Is Correct\n You just won 100$")
    else:
        print("Wrong Answer\n")


# print(questions[0])
# ans1 = input("Enter Option:\n")
# if ans1 == answers[0]:
#     print("Congragulations!\nAnswer Is Correct\n You just won 100$")
# else:
#     print("Wrong Answer\n")


# print(questions[1])
# ans2 = input("Enter Option:\n")
# if ans2 == answers[1]:
#     print("Congragulations!\nAnswer Is Correct\n You just won 100$")
# else:
#     print("Wrong Answer\n")


# print(questions[2])
# ans3 = input("Enter Option:\n")
# if ans3 == answers[2]:
#     print("Congragulations!\nAnswer Is Correct\n You just won 100$")
# else:
#     print("Wrong Answer\n")


# print(questions[3])
# ans4 = input("Enter Option:\n")
# if ans4 == answers[3]:
#     print("Congragulations!\nAnswer Is Correct\n You just won 100$")
# else:
#     print("Wrong Answer")
