# here in this code I will have bmw models of m8 m5 m440i and i4 and then will check if for example its in the list or not.


# the return is the preset models

def initialmodel():
    return ["M8", "M5", "M440i", "i4"]

# This checks to see if these models are in the list
def findmodel(models, modelfinding):
    return modelfinding in models

# This brings the preset list again
def main():
    models = initialmodel()

    # Loop to either leave or carry on code
    while True:
        modelfinding = input("Which BMW model are you after? Please type 'leave' to exit process: ")

        if modelfinding == 'leave':
            print("Shutting search down")
            break

        # This will now check if the model is in the list
        if findmodel(models, modelfinding):
            print(modelfinding + " is available.")
        else:
            print(modelfinding + " is not available.")

if __name__ == "__main__":
    main()



# this code was pretty annoying, I kept mixing up model and modelfinding and didn't know why it was incorrect. This code includes definitions, error handling and loops.