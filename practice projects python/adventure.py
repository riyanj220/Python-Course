import time

def introduction():
    choice = input("Do you want to play Text Adventure game? (yes/no) ").lower()
    if choice != "no":
        name = input("Type your name: ").upper()
        print("Welcome", name, "to this adventure!")
        print()
    else:
        quit()

def instructions():
    print("***INSTRUCTIOS FOR TEXT ADVENTURE GAME***")
    print("1. After every sitaution there are brackets with choices , make sure to enter them accurately")
    print("2. Your total time will be calculated and displayed , so make sure to keep it in your mind")
    print("3. You goal is to find a hidden treasure Good Luck!")
    print()


start_time=time.time()

def dirt_road():
    print()
    answer = input(
        "You are on a dirt road, and it has come to an end. Which way would you like to go? (left/right) "
    ).lower()

    if answer == "left":
        explore_river()
    elif answer == "right":
        bridge()
    else:
        print("Not a valid option. You Lose!")


def explore_river():
    print()
    answer = input(
        "You come to a river. Do you want to walk around it or swim across? (walk/swim) "
    ).lower()

    if answer == "swim":
        doplhin()
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and you lost the game. ")
        total_time()
    else:
        print("Not a valid option. You Lose!")


def doplhin():
    print()
    print("During swimming ,you encountered a freindly dolphin that landed you on the coast line")
    answer=input("Do you want to take rest or continue your journey? (rest/continue) ").lower()

    if answer=="rest":
        print("While You were resting , a lion attacked you and you were killed")
        total_time()

    elif answer=="continue":
        old_man_house()

    else:
        print("Not a valid option. You Lose!")


def old_man_house():
    print()
    answer=input("You reached an old man's house ,He offered you a dinner with him , Do you want to accept his offer? (yes/no) ").lower()

    if answer=="no":
        print("You died of hunger. You Lose!")
        total_time()
    elif answer=="yes":
        print("The food was mixed with poison and you died! You Lose!")
        total_time()
    else:
        print("Not a valid option. You Lose!")
    

def bridge():
    print()
    answer = input(
        "You come to a bridge. It looks wobbly. Do you want to cross it or head back? (cross/back) "
    ).lower()

    if answer == "back":
        print("You went back and lose.")
        total_time()
    elif answer == "cross":
        meet_stranger()
    else:
        print("Not a valid option! You Lose!")


def meet_stranger():
    print()
    answer = input(
        "You crossed the bridge and meet a stranger. Do you want to talk to him? (yes/no) "
    ).lower()

    if answer == "yes":
        mystery_box()
    elif answer == "no":
        print("As you turned away, the stranger revealed a crucial piece of information. Regretfully, You Lose!")
        total_time()
    else:
        print("Not a valid option! You Lose!")


def mystery_box():
    print()
    answer=input("The stranger gave you a mystery box that looks suspicious, do you want to open it or throw it aaway? (open/throw) ").lower()
    if answer=="open":
        tresure_map()
    elif answer=="throw":
        print("That box contained a tresure map ! You Lose!")
        total_time()
    else:
        print("Not a valid option! You Lose!")


def tresure_map():
    print()
    print("You found a hidden treasure map in the mystery box!")
    answer=input("Decide when do you want to explore the treasure map? (morning/evening) ").lower()

    if answer=="evening":
        print("You were eaten by a tiger ! You Lose !")

    elif answer =="morning":
        location()

    else:
        print("Not a valid option! You Lose!")
        
def location():
    print()
    print("You reached the location successfully and found The treasure")
    answer=input("Its evening time , Do you want to sleep or head back? (sleep/back) ")

    if answer=="sleep":
        conclusion()

    elif answer=="back":
        print("You are robbed by robbers! You Lose!")

    else:
        print("Not a valid option! You Lose!")



def conclusion():
    print()
    print("You slept well, and reached home safely! You Won!")
    total_time() 

def total_time():
    end_time=time.time()
    elapsed_time=end_time- start_time

    if elapsed_time<60:
        print(f"Total time taken to Play: {elapsed_time: .2f} seconds")

    else:
        minutes=int(elapsed_time//60)
        seconds =elapsed_time%60
        print(f"Total time taken to Play: {minutes} minutes and {seconds:.2f} seconds") 

def main():
    introduction()
    instructions()
    time.sleep(10)
    dirt_road()



if __name__ == "__main__":
    main()




