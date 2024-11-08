# here I will make a BMW dealership that lists and presents the prices of each car

# I will begin the list below

cars = "M8 Competition","M5 Competition", "M440i", "i4"
print("The vehicles we have are", cars)

# now I will give the cars the value using the dictionary
values = {"M8 Competition": "£134,205", "M5 Competition": "£98,095", "M440i": "£53,200", "i4": "£50,365"}


carpick = input("What are you interesred in today? ")

# now I will add conditionals
# the 
if carpick == "M8 Competition":
    print(f"Amazing choice " + carpick + " and this is valued at " +values["M8 Competition"])

elif carpick == "M5 competition":
    print(f"Great choice " + carpick + " and this is valued at " +values["M5 Competition"])

elif carpick == "M440i":
    print(f"Eh well " + carpick + " is valued at" +values["M8 Competition"] + " not a real M but oh well")

elif carpick == "i4":
    print(f"Haha " + carpick + " is valued at " +values["M8 Competition"] + " electric car what a loser")

else:
    print("Not available here sorry")


# here I took quite a bit, wasn't sure on how to remove the brackets and apostrophe from the vehicle list but did what I could