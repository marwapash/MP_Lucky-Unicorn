# Ask the user if they have played before
show_instructions = input("Have you played this game before?").lower()

# If they say yes output 'programme continue'
if show_instructions == "yes":
    print("Program continues")

elif show_instructions == "y":
    print("Program continues")

elif show_instructions == "no":
    print("Display instructions")

elif show_instructions == "n":
    print("Display instructions")

# if they say no, output 'display instructions'
else:
    print("Please answer yes / no")
