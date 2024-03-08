from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import pyttsx3
import cv2

user_name=None
next_screen=None
new_window=None
dirt_window=None
explore_river_window=None
walk_window=None
doplhin_window=None
bridge_window=None
yes_window=None
no_window=None
bridge_window=None
cross_window=None
stranger_no_window=None
stranger_yes_window=None
throw_window=None
open_window=None
evening_window=None
morning_window=None
bridge_back_window=None
win_window=None
treasure_coming=None
members_window=None

def speak_text(text,pitch=1.0):
    engine=pyttsx3.init()
    engine.setProperty('rate',150)
    engine.setProperty('speed',1.3) 
    engine.setProperty('pitch',pitch) 

    engine.say(text)
    engine.runAndWait()


def group_members():
    global root,members_window
    root.withdraw()

    members_window =Toplevel(root)
    members_window.title("Instructions")
    members_window.geometry('900x700')
    members_window.maxsize(900,700)

    members_pic = Image.open("members.png").resize((900, 700))
    members_pic_tk = ImageTk.PhotoImage(members_pic)

    members_pic_label = Label(members_window, image=members_pic_tk)
    members_pic_label.image = members_pic_tk  
    members_pic_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    members_continue_button =Button(members_window,text="Continue",command=continue_clicked,bg='light green', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="white")
    members_continue_button.place(relx=0.9,rely=0.9,anchor=SE)

def continue_clicked():
    global next_screen,user_name,members_window
    members_window.withdraw()

    next_screen =Toplevel(root)
    next_screen.title("Introduction")
    next_screen.configure(background='#9CFF33')

    name_frame = ImageTk.PhotoImage(Image.open("name_frame.png").resize((900,700)))
    name_frame_label = Label(next_screen, image=name_frame)
    name_frame_label.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    label_intro=Label(next_screen,text="Enter your name ",font=('Comic Sans MS',22),bg='white', bd=2, relief="solid")
    label_intro.configure(width=15,height=1)
    label_intro.place(relx=0.44,rely=0.35,anchor=CENTER)

    entry_name=Entry(next_screen,width=30,bd=2,font=('Comic Sans MS', 18), justify="center", relief="solid",insertofftime=1)
    entry_name.pack(side=TOP,anchor=CENTER)
    entry_name.place(relx=0.44,rely=0.45,anchor=CENTER)

    button_submit=Button(next_screen,text="Submit",command=lambda:submit_clicked(entry_name.get()),bg="yellow",fg='black',width=10, bd=2,relief="raised",font=('Comic Sans MS', 16,'bold'),activebackground="#cddc39")
    button_submit.pack(side=TOP,anchor=CENTER)
    button_submit.place(relx=0.44,rely=0.55,anchor=CENTER)

    next_screen.geometry('900x700')
    next_screen.maxsize(900,700)
    next_screen.mainloop()

def submit_clicked(name):

    global next_screen,user_name,new_window
    user_name=name
    next_screen.withdraw()

    new_window=Toplevel(root)
    new_window.title("Instructions")
    new_window.geometry('900x700')
    new_window.maxsize(900,700)

    instruction_pic = Image.open("instruction_pic.jpg").resize((900, 700))
    instruction_pic_tk = ImageTk.PhotoImage(instruction_pic)

    instruction_pic_label = Label(new_window, image=instruction_pic_tk)
    instruction_pic_label.image = instruction_pic_tk  
    instruction_pic_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    text_to_speak=f"Welcome! {user_name} to text adventure game."
    label_intro=Label(new_window,text=text_to_speak,font=('Comic Sans MS',20),bg='white', bd=2, relief="solid")
    label_intro.configure(width=38,height=2)
    label_intro.place(relx=0.5,rely=0.2,anchor=CENTER)

    new_window.after(90,speak_text,text_to_speak)

    label_instuctions=Label(new_window,text="""***INSTRUCTIONS FOR TEXT ADVENTURE GAME***\n\n1) After every sitaution there are 2 options , make sure to choose them wisely\n\n2) You goal is to find a hidden treasure Good Luck!""",font=('Comic Sans MS',12),bg='white', bd=2, relief="solid",wraplength=550)
    label_instuctions.configure(width=80,height=8)
    label_instuctions.place(relx=0.5,rely=0.5,anchor=CENTER)

    ins_continue_button =Button(new_window,text="Continue",command=dirt_road,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39")
    ins_continue_button.place(relx=0.5,rely=0.7,anchor=CENTER)

def dirt_road():
    global new_window,dirt_window
    new_window.withdraw()

    dirt_window =Toplevel(root)
    dirt_window.geometry('900x700')
    dirt_window.maxsize(900,700)
    dirt_window.title("Dirt road")

    dirt_road_pic = Image.open("dirt_road_pic.jpeg").resize((900, 700))
    dirt_road_pic_tk = ImageTk.PhotoImage(dirt_road_pic)

    dirt_road_label = Label(dirt_window, image=dirt_road_pic_tk)
    dirt_road_label.image = dirt_road_pic_tk  
    dirt_road_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    text_to_speak="You are on a dirt road, and it has come to an end. Which way would you like to go?"
    dirt_window_label=Label(dirt_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    dirt_window_label.configure(width=40,height=3)
    dirt_window_label.place(relx=0.5,rely=0.4,anchor=CENTER)
    dirt_window.after(90,speak_text,text_to_speak)

    left_button=Button(dirt_window,text="Left",command=explore_river,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    left_button.pack(pady=10)
    left_button.place(relx=0.4,rely=0.6,anchor=CENTER)

    right_button=Button(dirt_window,text="Right",command=bridge,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    right_button.pack(pady=10)
    right_button.place(relx=0.6,rely=0.6,anchor=CENTER)

def explore_river():
    global explore_river_window,dirt_window
    dirt_window.withdraw()

    explore_river_window =Toplevel(root)
    explore_river_window.geometry('900x700')
    explore_river_window.maxsize(900,700)
    explore_river_window.title("Explore River")

    explore_river_pic = Image.open("explore_river_pic.jpg").resize((900, 700))
    explore_river_pic_tk = ImageTk.PhotoImage(explore_river_pic)

    explore_river_pic_label = Label(explore_river_window, image=explore_river_pic_tk)
    explore_river_pic_label.image = explore_river_pic_tk 
    explore_river_pic_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    text_to_speak="You come to a river. Do you want to walk around it or swim across?"
    explore_river_label=Label(explore_river_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    explore_river_label.configure(width=40,height=3)
    explore_river_label.place(relx=0.5,rely=0.4,anchor=CENTER)
    explore_river_window.after(90,speak_text,text_to_speak)

    walk_button=Button(explore_river_window,text="Walk",command=explore_river_walk,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    walk_button.place(relx=0.4,rely=0.6,anchor=CENTER)

    swim_button=Button(explore_river_window,text="Swim",command=dolphin,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    swim_button.place(relx=0.6,rely=0.6,anchor=CENTER)

def explore_river_walk():
    global explore_river_window,walk_window
    explore_river_window.withdraw()

    walk_window=Toplevel(root)
    walk_window.geometry('900x700')
    walk_window.maxsize(900,700)
    walk_window.title("Try Again")
    walk_window.configure(background='#9CFF33')

    sad_emoji = Image.open("sad_emoji.jpg").resize((300, 300))
    sad_emoji_tk = ImageTk.PhotoImage(sad_emoji)
    sad_emoji_label = Label(walk_window, image=sad_emoji_tk)
    sad_emoji_label.image = sad_emoji_tk 
    sad_emoji_label.place(relx=0.15, rely=0.8, anchor=CENTER)

    text_to_speak="You walked for many miles, ran out of water, and you lost the game."
    walk_window_label=Label(walk_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    walk_window_label.configure(width=40,height=3)
    walk_window_label.place(relx=0.5,rely=0.3,anchor=CENTER)
    walk_window.after(90,speak_text,text_to_speak)

    exit_button=Button(walk_window,text="Exit",command=exit,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    exit_button.place(relx=0.4,rely=0.5,anchor=CENTER)

    play_again=Button(walk_window,text="Play Again",command=lambda: [walk_window.withdraw(),dirt_road()],bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    play_again.place(relx=0.6,rely=0.5,anchor=CENTER)

def exit():
    quit()

def dolphin():
    global explore_river_window,doplhin_window
    explore_river_window.withdraw()

    doplhin_window =Toplevel(root)
    doplhin_window.geometry('900x700')
    doplhin_window.maxsize(900,700)
    doplhin_window.title("Friendly Dolphin")

    dolphin_pic = Image.open("dolphin_pic.jpg").resize((900, 700))
    dolphin_pic_tk = ImageTk.PhotoImage(dolphin_pic)

    dolphin_pic_label = Label(doplhin_window, image=dolphin_pic_tk)
    dolphin_pic_label.image = dolphin_pic_tk 
    dolphin_pic_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    text_to_speak ="During swimming ,you encountered a friendly dolphin that landed you on the coast line\nDo you want to take rest or continue your journey?"
    explore_label=Label(doplhin_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    explore_label.configure(width=38,height=5)
    explore_label.place(relx=0.5,rely=0.4,anchor=CENTER)
    doplhin_window.after(90,speak_text,text_to_speak)

    rest_button=Button(doplhin_window,text="Rest",command=rest,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    rest_button.place(relx=0.4,rely=0.7,anchor=CENTER)

    continue_button=Button(doplhin_window,text="Continue",command=continue_journey,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    continue_button.place(relx=0.6,rely=0.7,anchor=CENTER)

def rest():
    global doplhin_window,yes_window
    doplhin_window.withdraw()

    yes_window=Toplevel(root)
    yes_window.geometry('900x700')
    yes_window.maxsize(900,700)
    yes_window.title("Try Againn")
    yes_window.configure(background='#9CFF33')

    text_to_speak="While You were resting , a lion attacked you and you were killed."
    yes_window_label=Label(yes_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    yes_window_label.configure(width=40,height=3)
    yes_window_label.place(relx=0.5,rely=0.3,anchor=CENTER)
    yes_window.after(90,speak_text,text_to_speak)

    sad_emoji = Image.open("sad_emoji.jpg").resize((300, 300))
    sad_emoji_tk = ImageTk.PhotoImage(sad_emoji)
    sad_emoji_label = Label(yes_window, image=sad_emoji_tk)
    sad_emoji_label.image = sad_emoji_tk 
    sad_emoji_label.place(relx=0.15, rely=0.8, anchor=CENTER)

    exit_button=Button(yes_window,text="Exit",command=exit,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    exit_button.place(relx=0.4,rely=0.5,anchor=CENTER)

    play_again=Button(yes_window,text="Play Again",command=lambda: [yes_window.withdraw(),dirt_road()],bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    play_again.place(relx=0.6,rely=0.5,anchor=CENTER)

def continue_journey():
    global doplhin_window,old_man_window
    doplhin_window.withdraw()

    old_man_window =Toplevel(root)
    old_man_window.geometry('900x700')
    old_man_window.maxsize(900,700)
    old_man_window.title("Old man's house")

    old_mam_pic = Image.open("old_man_pic.jpeg").resize((900, 800))
    old_man_pic_tk = ImageTk.PhotoImage(old_mam_pic)

    old_mam_pic_label = Label(old_man_window, image=old_man_pic_tk)
    old_mam_pic_label.image = old_man_pic_tk 
    old_mam_pic_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    text_to_speak="You reached an old man's house , He offered you a dinner with him , Do you want to accept his offer?"
    old_man_window_label=Label(old_man_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    old_man_window_label.configure(width=38,height=5)
    old_man_window_label.place(relx=0.5,rely=0.4,anchor=CENTER)
    old_man_window.after(90,speak_text,text_to_speak)

    yes_button=Button(old_man_window,text="Yes",bg='yellow',command=yes, fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    yes_button.place(relx=0.4,rely=0.7,anchor=CENTER)

    no_button=Button(old_man_window,text="No",command=no,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    no_button.place(relx=0.6,rely=0.7,anchor=CENTER)

def no():
    global old_man_window,no_window
    old_man_window.withdraw()

    no_window=Toplevel(root)
    no_window.geometry('900x700')
    no_window.maxsize(900,700)
    no_window.title("Try Againn")
    no_window.configure(background='#9CFF33')

    sad_emoji = Image.open("sad_emoji.jpg").resize((300, 300))
    sad_emoji_tk = ImageTk.PhotoImage(sad_emoji)
    sad_emoji_label = Label(no_window, image=sad_emoji_tk)
    sad_emoji_label.image = sad_emoji_tk 
    sad_emoji_label.place(relx=0.15, rely=0.8, anchor=CENTER)

    text_to_speak ="You died of hunger. You Lose!"
    no_window_label=Label(no_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    no_window_label.configure(width=40,height=3)
    no_window_label.place(relx=0.5,rely=0.3,anchor=CENTER)
    no_window.after(90,speak_text,text_to_speak)

    exit_button=Button(no_window,text="Exit",command=exit,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    exit_button.place(relx=0.4,rely=0.5,anchor=CENTER)

    play_again=Button(no_window,text="Play Again",command=lambda: [no_window.withdraw(),dirt_road()],bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    play_again.place(relx=0.6,rely=0.5,anchor=CENTER)
    
def yes():
    global old_man_window,yes_window
    old_man_window.withdraw()

    yes_window=Toplevel(root)
    yes_window.geometry('900x700')
    yes_window.maxsize(900,700)
    yes_window.title("Try Againn")
    yes_window.configure(background='#9CFF33')

    sad_emoji = Image.open("sad_emoji.jpg").resize((300, 300))
    sad_emoji_tk = ImageTk.PhotoImage(sad_emoji)
    sad_emoji_label = Label(yes_window, image=sad_emoji_tk)
    sad_emoji_label.image = sad_emoji_tk 
    sad_emoji_label.place(relx=0.15, rely=0.8, anchor=CENTER)

    text_to_speak="The food was mixed with poison and you died! You Lost the game!"
    yes_window_label=Label(yes_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    yes_window_label.configure(width=40,height=3)
    yes_window_label.place(relx=0.5,rely=0.3,anchor=CENTER)
    yes_window.after(90,speak_text,text_to_speak)

    exit_button=Button(yes_window,text="Exit",command=exit,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    exit_button.place(relx=0.4,rely=0.5,anchor=CENTER)

    play_again=Button(yes_window,text="Play Again",command=lambda: [yes_window.withdraw(),dirt_road()],bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    play_again.place(relx=0.6,rely=0.5,anchor=CENTER)


def bridge():
    global dirt_window,bridge_window
    dirt_window.withdraw()

    bridge_window =Toplevel(root)
    bridge_window.geometry('900x700')
    bridge_window.maxsize(900,700)
    bridge_window.title("Bridge")

    bridge_pic = Image.open("bridge_pic.jpeg").resize((900, 800))
    bridge_pic_tk = ImageTk.PhotoImage(bridge_pic)

    bridge_pic_label = Label(bridge_window, image=bridge_pic_tk)
    bridge_pic_label.image = bridge_pic_tk 
    bridge_pic_label.place(relx=0.5, rely=0.5, anchor=CENTER)
 
    text_to_speak="You come to a bridge. It looks wobbly. Do you want to cross it or go from down side?"
    bridge_window_label=Label(bridge_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    bridge_window_label.configure(width=38,height=5)
    bridge_window_label.place(relx=0.5,rely=0.4,anchor=CENTER)
    bridge_window.after(90,speak_text,text_to_speak)

    cross_button=Button(bridge_window,text="Cross",command=cross,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    cross_button.place(relx=0.4,rely=0.65,anchor=CENTER)

    head_back_button=Button(bridge_window,text="Down side",command=head_back,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    head_back_button.place(relx=0.6,rely=0.65,anchor=CENTER)

def head_back():
    global bridge_window,bridge_back_window
    bridge_window.withdraw()

    bridge_back_window=Toplevel(root)
    bridge_back_window.geometry('900x700')
    bridge_back_window.maxsize(900,700)
    bridge_back_window.title("Try Againn")
    bridge_back_window.configure(background='#9CFF33')

    sad_emoji = Image.open("sad_emoji.jpg").resize((300, 300))
    sad_emoji_tk = ImageTk.PhotoImage(sad_emoji)
    sad_emoji_label = Label(bridge_back_window, image=sad_emoji_tk)
    sad_emoji_label.image = sad_emoji_tk 
    sad_emoji_label.place(relx=0.15, rely=0.8, anchor=CENTER)

    text_to_speak="Your foot slipped and you fell from the height , You lost the game!"
    bridge_back_window_label=Label(bridge_back_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    bridge_back_window_label.configure(width=40,height=4)
    bridge_back_window_label.place(relx=0.5,rely=0.3,anchor=CENTER)
    bridge_back_window.after(90,speak_text,text_to_speak)

    exit_button=Button(bridge_back_window,text="Exit",command=exit,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    exit_button.place(relx=0.4,rely=0.5,anchor=CENTER)

    play_again=Button(bridge_back_window,text="Play Again",command=lambda: [bridge_back_window.withdraw(),dirt_road()],bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    play_again.place(relx=0.6,rely=0.5,anchor=CENTER)

def cross():
    global bridge_window,cross_window
    bridge_window.withdraw()

    cross_window =Toplevel(root)
    cross_window.geometry('900x700')
    cross_window.maxsize(900,700)
    cross_window.title("Bridge")

    stranger_pic = Image.open("stranger_pic.jpg").resize((1400, 900))
    stranger_pic_tk = ImageTk.PhotoImage(stranger_pic)

    stranger_pic_label = Label(cross_window, image=stranger_pic_tk)
    stranger_pic_label.image = stranger_pic_tk 
    stranger_pic_label.place(relx=0.5, rely=0.5, anchor=CENTER)
 
    text_to_speak="You crossed the bridge and meet a stranger. Do you want to talk to him?"
    cross_window_label=Label(cross_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    cross_window_label.configure(width=38,height=5)
    cross_window_label.place(relx=0.5,rely=0.4,anchor=CENTER)
    cross_window.after(90,speak_text,text_to_speak)

    yes_button=Button(cross_window,text="Yes",bg='yellow', command=stranger_yes,fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    yes_button.place(relx=0.4,rely=0.65,anchor=CENTER)

    no_button=Button(cross_window,text="No",bg='yellow',command=stranger_no, fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    no_button.place(relx=0.6,rely=0.65,anchor=CENTER)

def stranger_no():
    global cross_window,stranger_no_window
    cross_window.withdraw()

    stranger_no_window=Toplevel(root)
    stranger_no_window.geometry('900x700')
    stranger_no_window.maxsize(900,700)
    stranger_no_window.title("Try Againn")
    stranger_no_window.configure(background='#9CFF33')

    sad_emoji = Image.open("sad_emoji.jpg").resize((300, 300))
    sad_emoji_tk = ImageTk.PhotoImage(sad_emoji)
    sad_emoji_label = Label(stranger_no_window, image=sad_emoji_tk)
    sad_emoji_label.image = sad_emoji_tk 
    sad_emoji_label.place(relx=0.15, rely=0.8, anchor=CENTER)

    text_to_speak="As you turned away, the stranger revealed a crucial piece of information. You Lost the game!"
    stranger_no_window_label=Label(stranger_no_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    stranger_no_window_label.configure(width=40,height=4)
    stranger_no_window_label.place(relx=0.5,rely=0.3,anchor=CENTER)
    stranger_no_window.after(90,speak_text,text_to_speak)

    exit_button=Button(stranger_no_window,text="Exit",command=exit,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    exit_button.place(relx=0.4,rely=0.5,anchor=CENTER)

    play_again=Button(stranger_no_window,text="Play Again",command=lambda:[stranger_no_window.withdraw(),dirt_road()],bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    play_again.place(relx=0.6,rely=0.5,anchor=CENTER)

def stranger_yes():
    global cross_window,stranger_yes_window
    cross_window.withdraw()

    stranger_yes_window =Toplevel(root)
    stranger_yes_window.geometry('900x700')
    stranger_yes_window.maxsize(900,700)
    stranger_yes_window.title("Mystery box")

    mystery_box_pic = Image.open("mystery_box_pic.jpg").resize((1400, 900))
    mystery_box_pic_tk = ImageTk.PhotoImage(mystery_box_pic)

    mystery_box__pic_label = Label(stranger_yes_window, image=mystery_box_pic_tk)
    mystery_box__pic_label.image = mystery_box_pic_tk 
    mystery_box__pic_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    text_to_speak="The stranger gave you a mystery box that looks suspicious, do you want to open it or throw it away?"
    stranger_yes_window_label=Label(stranger_yes_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    stranger_yes_window_label.configure(width=38,height=5)
    stranger_yes_window_label.place(relx=0.5,rely=0.4,anchor=CENTER)
    stranger_yes_window.after(90,speak_text,text_to_speak)

    open_button=Button(stranger_yes_window,text="Open",command=open,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    open_button.place(relx=0.4,rely=0.65,anchor=CENTER)

    throw_button=Button(stranger_yes_window,text="Throw",command=throw,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    throw_button.place(relx=0.6,rely=0.65,anchor=CENTER)

def throw():
    global stranger_yes_window,throw_window
    stranger_yes_window.withdraw()

    throw_window=Toplevel(root)
    throw_window.geometry('900x700')
    throw_window.maxsize(900,700)
    throw_window.title("Try Againn")
    throw_window.configure(background='#9CFF33')

    sad_emoji = Image.open("sad_emoji.jpg").resize((300, 300))
    sad_emoji_tk = ImageTk.PhotoImage(sad_emoji)
    sad_emoji_label = Label(throw_window, image=sad_emoji_tk)
    sad_emoji_label.image = sad_emoji_tk 
    sad_emoji_label.place(relx=0.15, rely=0.8, anchor=CENTER)

    text_to_speak="That box contained the treasure map ! You Lost the game!"
    throw_window_label=Label(throw_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    throw_window_label.configure(width=40,height=4)
    throw_window_label.place(relx=0.5,rely=0.3,anchor=CENTER)
    throw_window.after(90,speak_text,text_to_speak)

    exit_button=Button(throw_window,text="Exit",command=exit,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    exit_button.place(relx=0.4,rely=0.5,anchor=CENTER)

    play_again=Button(throw_window,text="Play Again",command=lambda: [throw_window.withdraw(),dirt_road()],bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    play_again.place(relx=0.6,rely=0.5,anchor=CENTER)

def open():
    global stranger_yes_window,open_window
    stranger_yes_window.withdraw()

    open_window =Toplevel(root)
    open_window.geometry('900x700')
    open_window.maxsize(900,700)
    open_window.title("Treasure Map")

    treasure_map_pic = Image.open("treasure_map_pic.jpg").resize((1400, 900))
    treasure_map_pic_tk = ImageTk.PhotoImage(treasure_map_pic)

    treasure_map_pic_label = Label(open_window, image=treasure_map_pic_tk)
    treasure_map_pic_label.image = treasure_map_pic_tk 
    treasure_map_pic_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    text_to_speak="You found a hidden treasure map in the mystery box!\nDecide when do you want to explore the treasure map?"
    open_window_label=Label(open_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    open_window_label.configure(width=38,height=5)
    open_window_label.place(relx=0.5,rely=0.4,anchor=CENTER)
    open_window.after(90,speak_text,text_to_speak)

    morning_button=Button(open_window,text="Morning",bg='yellow',command=morning,fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    morning_button.place(relx=0.4,rely=0.65,anchor=CENTER)

    evening_button=Button(open_window,text="Evening",command=evening,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    evening_button.place(relx=0.6,rely=0.65,anchor=CENTER)

def evening():
    global open_window,evening_window
    open_window.withdraw()

    evening_window=Toplevel(root)
    evening_window.geometry('900x700')
    evening_window.maxsize(900,700)
    evening_window.title("Try Againn")
    evening_window.configure(background='#9CFF33')

    sad_emoji = Image.open("sad_emoji.jpg").resize((300, 300))
    sad_emoji_tk = ImageTk.PhotoImage(sad_emoji)
    sad_emoji_label = Label(evening_window, image=sad_emoji_tk)
    sad_emoji_label.image = sad_emoji_tk 
    sad_emoji_label.place(relx=0.15, rely=0.8, anchor=CENTER)

    text_to_speak="during your exploring in evening You were eaten by a tiger ! You Lost the game!"
    evening_window_label=Label(evening_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white', wraplength=550)
    evening_window_label.configure(width=40,height=4)
    evening_window_label.place(relx=0.5,rely=0.3,anchor=CENTER)
    evening_window.after(90,speak_text,text_to_speak)

    exit_button=Button(evening_window,text="Exit",command=exit,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    exit_button.place(relx=0.4,rely=0.5,anchor=CENTER)

    play_again=Button(evening_window,text="Play Again",command=lambda: [evening_window.withdraw(),dirt_road()],bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    play_again.place(relx=0.6,rely=0.5,anchor=CENTER)

def morning():
    global open_window,morning_window
    open_window.withdraw()

    morning_window =Toplevel(root)
    morning_window.geometry('900x700')
    morning_window.maxsize(900,700)
    morning_window.title("Treasure Location")

    treasure_location_pic = Image.open("treasure_location_pic.jpg").resize((1100, 900))
    treasure_location_pic_tk = ImageTk.PhotoImage(treasure_location_pic)

    treasure_location_pic_label = Label(morning_window, image=treasure_location_pic_tk)
    treasure_location_pic_label.image = treasure_location_pic_tk 
    treasure_location_pic_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    text_to_speak="You reached the location successfully and found The treasure\nIts night time , Do you want to sleep or go back to your home?"
    morning_window_label=Label(morning_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white',wraplength=550)
    morning_window_label.configure(width=38,height=5)
    morning_window_label.place(relx=0.5,rely=0.4,anchor=CENTER)
    morning_window.after(90,speak_text,text_to_speak)

    sleep_button=Button(morning_window,text="Sleep",command=win,bg='yellow',fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    sleep_button.place(relx=0.4,rely=0.65,anchor=CENTER)

    back_button=Button(morning_window,text="Back",bg='yellow', command=treasure_coming_back,fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    back_button.place(relx=0.6,rely=0.65,anchor=CENTER)

def win():
    global win_window,morning_window
    morning_window.withdraw()

    win_window=Toplevel(root)
    win_window.geometry('900x700')
    win_window.maxsize(900,700)
    win_window.title("You Won")
    win_window.configure(background='#9CFF33')

    congrats_pic = Image.open("congrats_pic.jpg").resize((900, 1000))
    congrats_pic_tk = ImageTk.PhotoImage(congrats_pic)

    congrats_pic_label = Label(win_window, image=congrats_pic_tk)
    congrats_pic_label.image = congrats_pic_tk 
    congrats_pic_label.place(relx=0.5, rely=0.7, anchor=CENTER)

    text_to_speak="You slept well, and reached home safely!\nYou Win!"
    win_window_label=Label(win_window,text=text_to_speak,font=('Comic Sans MS',18),bg='white', bd=3,wraplength=550)
    win_window_label.configure(width=40,height=4)
    win_window_label.place(relx=0.5,rely=0.4,anchor=CENTER)
    win_window.after(90,speak_text,text_to_speak)

    exit_button=Button(win_window,text="Exit",command=exit,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    exit_button.place(relx=0.5,rely=0.65,anchor=CENTER)

def treasure_coming_back():
    global treasure_coming,morning_window
    morning_window.withdraw()

    treasure_coming=Toplevel(root)
    treasure_coming.geometry('900x700')
    treasure_coming.maxsize(900,700)
    treasure_coming.title("Try again")
    treasure_coming.configure(background='#9CFF33')

    sad_emoji = Image.open("sad_emoji.jpg").resize((300, 300))
    sad_emoji_tk = ImageTk.PhotoImage(sad_emoji)
    sad_emoji_label = Label(treasure_coming, image=sad_emoji_tk)
    sad_emoji_label.image = sad_emoji_tk 
    sad_emoji_label.place(relx=0.15, rely=0.8, anchor=CENTER)

    text_to_speak="You were robbed by robbers at midnight! You Lost the game!"
    treasure_coming_label=Label(treasure_coming,text=text_to_speak,bg= "white",font=('Comic Sans MS',18), bd=3,wraplength=550)
    treasure_coming_label.configure(width=40,height=4)
    treasure_coming_label.place(relx=0.5,rely=0.3,anchor=CENTER)
    treasure_coming.after(90,speak_text,text_to_speak)

    exit_button=Button(treasure_coming,text="Exit",command=exit,bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    exit_button.place(relx=0.4,rely=0.5,anchor=CENTER)

    play_again=Button(treasure_coming,text="Play Again",command=lambda: [treasure_coming.withdraw(),dirt_road()],bg='yellow', fg='black', font=('Comic Sans MS', 16,'bold'),bd=2, relief="raised",activebackground="#cddc39",width=10,height=2)
    play_again.place(relx=0.6,rely=0.5,anchor=CENTER)


root=Tk()
root.title('Text Adventure Game')

logo_image=PhotoImage(file='adventure_logo.png')
root.tk.call('wm','iconphoto',root._w,logo_image)

root.geometry('900x700')
root.maxsize(900,700)
root.configure(background='#9CFF33')

main_img = ImageTk.PhotoImage(Image.open('adventure_logo.png'))
main_img_label =Label(root,image=main_img)
main_img_label.place(x=0, y=0, relwidth=1, relheight=1)
main_img_label.pack()

continue_button =Button(root,text="Continue",command=group_members,bg='#33A5FF', fg='white', font=('Comic Sans MS', 16))
continue_button.pack(side=BOTTOM,padx =10,pady=10)
continue_button.place(relx=0.9,rely=0.9,anchor=SE)

root.mainloop()