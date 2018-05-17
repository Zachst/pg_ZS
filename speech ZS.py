import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What's your name?")

answer = pg.prompt("Enter your name.")

speak.speak("Hello" + answer + " What's your favorite food?")

food = pg.prompt("enter your favorite food.")

if food == "Electricity":
    speak.Speak("Why you eating electricity?")

elif food == "Water":
                speak.Speak("water")

else:
                speak.Speak("you like to eat " + food + ". I'm still learning what that is.")


speak.speak("What video would you like to watch?")

video = pg.prompt("enter your video below.")

speak.speak("ok, let's look for " + video + " on YouTube and see what we find.")

wb.open("https://www.youtube.com/results?search_query=" + video)
