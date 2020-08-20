import pyttsx3 
import os

pyttsx3 .speak("welcome in my tools")

while True:
    pyttsx3.speak("chat with me your requirement")
    print("chat with me your requirement : ", end='')
    p=input()
    if("dont" in p):
        print("cant open application")    
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("chrome" in p):
        pyttsx3.speak("yes, here is chrome")
        os.system("chrome")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p)):
        pyttsx3.speak("yes, here is notepad")
        os.system("notepad")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("vlc" in p):
        pyttsx3.speak("yes, here is vlc")
        os.system("vlc")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("player" in p) or ("media" in p)):
        pyttsx3.speak("yes, here is wmplayer")
        os.system("wmplayer")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("Arduino" in p) or ("program" in p)):
        pyttsx3.speak("yes, here is Arduino")
        os.system("Arduino")
    elif (("run" in p) or ("launch" in p) or ("launch" in p) ) and (("paint" in p)):
        pyttsx3.speak("yes, here is paint")
        os.system("paint")
    elif ("exit" in p) or ("quit" in p):
        break
    else:
        print("dont support")
  