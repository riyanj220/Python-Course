print("Welcome to my computer quiz!".title())
playing = input("Do You Want To Play? ".title())


if playing.lower() != "yes":
    quit()
print("Okay! lets play :)".title())
score = 0


answer = input("what does CPU stand for? ".title())
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does GPU stands for? ".title())
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does RAM stand for? ".title())
if answer.lower() == "random accessing memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does PSU stand for? ".title())
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
