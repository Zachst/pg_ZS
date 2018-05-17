import random

number = random.randint(0,3)


words = ["Dark Voyager","The Reaper","Black Knight","Rex"]
hint1 = ["coolest looking person in fortnite season 3","the best character in fortnite season 3","the best character in fortnite season 2","looks like a t-rex but is a human"]
hint2 = ["is black and orange","is wearing a suit","is a knight","is green"]

secretword = words[number]

guess = ""
counter = 1

while True:
    print("Guess the secret word")
    print("Type 'hint1', 'hint2', 'first letter', or 'give up' for answer.")
    guess = input()

    if guess == secretword:
        print("You win!")
        print("It took you " + str(counter) + " guesses.")
        break
    elif guess == "hint1":
        print( hint1[number] )

    elif guess == "hint2":
        print( hint2[number] )

    elif guess == "first letter":
        print( secretword[0] )


    elif guess == "give up":
        print("Wow. you gave up")
        print("you failed " + str(counter) + " times.")
        break

    else:
        print("guess again.")
        counter += 1

