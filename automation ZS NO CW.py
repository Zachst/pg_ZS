import pyautogui as pg
import webbrowser
import time

sport = pg.prompt(
    """
What is your sport
a)Football 
b)Hockey
c)Basketball

""")

if sport == "a":
    category = pg.prompt(
        """
What is your favorite football team
a)Giants
b)Patriots
c)Eagles
d)Seahawks

        """)
if category == "a":
     webbrowser.open()
elif category == "b":
     webbrowser.open()
elif category == "c":
    webbrowser.open()
elif category == "d":
    webbrowser.open()
        

elif sport == "b":
    category = pg.prompt(
        """
What is your favorite hockey team
a)Bruins
b)Rangers
c)Golden Knights
""")


elif sport == "c":
    category = pg.prompt(
        """
What is your favorite Basketball team?
a)Jazz
b)Rockets
c)Warriors

""")
    if category == "a":
        webbrowser.open("https://www.youtube.com/watch?v=fIAXPvBraE8")
        webbrowser.open("http://www.espn.com/nba/player/_/id/3908809/donovan-mitchell")
    elif category == "b":
        webbrowser.open()
    elif category == "c":
        webbrowser.open()
    


 

