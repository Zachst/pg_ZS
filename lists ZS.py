name = "ZACH"


subjects = ["English", "Math", "Spanish","Science"]

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)



Worstplacestoland = ["wailing woods" , "Moisty Mire", "Dusty Depot", "Tomato Town"]

for i in Worstplacestoland:
    if i == "Wailing woods":
        print(i + " have fun chopping down trees at ")
        print("the worst place to land is" + i)
  
    


countries = ["Germany", "Spain" ,"New Zealand"]

for i in countries:
    print("I want to visit " + i)


        

movies = []

while True:
    print("What movie do you like? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("One of your favorite movies is " + i)
