import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=LqGMEN8XBWY","https://www.youtube.com/watch?v=LqGMEN8XBWY","https://www.youtube.com/watch?v=WLiyNVWREpQ"]

music = ["https://www.spotify.com/us/premium/?utm_source=us-en_bra""https://www.spotify.com/us/","https://soundcloud.com/"]

answer = pg.prompt(
"""
Which would you rather do
a) Watch Videos
b) Listen to music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)



elif answer == "b":
    for i in music:
        webbrowser.open(i)
        
