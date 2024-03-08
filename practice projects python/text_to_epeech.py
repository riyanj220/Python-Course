import pyttsx3

names = []

while True:
    ask = input("enter your name to get shoutout or type done to exit : ".lower())
    if ask == "done":
        break
    names.append(ask)


engine = pyttsx3.init()
engine.setProperty(
    "voice",
    "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
)

for name in names:
    shoutout = f"shoutout to {name}"
    engine.say(shoutout)
    engine.runAndWait()

engine.stop()


# _________________________________________________________________________
# agar me janna chahta hun ke system ke paas kon kon c voices available hy
# to yeh process hoga


# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty("voices")

# for voice in voices:
#     print("voice: ")
#     print(" . ID: ", voice.id)
#     print(" - Name:", voice.name)
#     print(" - Languages:", voice.languages)
#     print(" - Gender:", voice.gender)
#     print(" - Age:", voice.age)
