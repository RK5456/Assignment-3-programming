
# here this code will be carrying out area of rectangles and allow the user to find out the squared length

# I have used the float function to allow the user to type in more complex numbers such as decimals

length = float(input("What is the length of the rectange in meters? "))
width = float(input("What is the width of the rectangle in meters? "))


# this will carry out the multiplication
area = length * width

print("The area is ", area,"m^2")

# here I thought of adding the conditionals part

if area > 50:
    print("The area of this rectangle is big")

elif 20 <= area <= 49:
    print("This is a reasonable sized rectangle")

else:
    print("This is a small rectangle")
        