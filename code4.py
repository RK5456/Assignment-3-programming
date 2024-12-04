# here I will use a modulo operation and case for BMW HP recognition, if the remainder is 0 its the best and below it becomes more fuel economy or not recognised
# note to self: this uses python 3.10 and higher, code was simulated on a higher source.

def bmwhp(hp):
    # match is used to find horsepower of cars and its levels
    match hp % 4:
        case 0:
            return "You've got an M Power beast! This BMW is built for the track."
        case 1:
            return "This is a classic BMW with balanced performance and style."
        case 2:
            return "Your BMW is a luxury model with smooth, effortless power."
        case 3:
            return "This BMW is tuned for efficiency with a sporty edge."
        case _:
            return "Hmm, that horsepower doesn't match any BMW in our records!"

# this is the inputs and outputs
horsepower = int(input("Enter your BMW's horsepower: "))  
print(bmwhp(horsepower))
