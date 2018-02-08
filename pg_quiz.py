import pyautogui as pg
import time
import webbrowser

points = 0

# Question 1

answer = pg.prompt(
"""

Do you like the state New York or California?

a) California
b) New York 
c) both
"""
    )


# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3





# Question 2

answer = pg.prompt(
"""

Do you like football or basketball?

a) Football
b) basketball
c) both
"""
    )


# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3




# Question 3

answer = pg.prompt(
"""

do you like college or profesional sports?
a) college
b) profesional
c) both 
"""
    )


# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3



# Question 4

answer = pg.prompt(
"""

Do you like blue or red?

a) blue
b) red
c) both
"""
    )


# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3 




# END OF SURVEY

#UCLA
if points < 6:
    pg.alert("you are the UCLA bruins")
    webbrowser.open("https://media.giphy.com/media/131IV4aVocU9DG/giphy.gif")

#New York Knicks
elif points >= 6 and points < 9:
    pg.alert("you are the New York Knicks")
    webbrowser.open("https://www.youtube.com/watch?v=d8FYUdPPUy4")

#New York Giants and La Clippers
elif points >= 9:
    pg.alert("you are the New York Giants and LA Clippers")
    webbrowser.open("https://avatars.mds.yandex.net/get-pdb/472427/fe9c684c-77b5-4eaa-afbf-687d81d79438/orig")


































