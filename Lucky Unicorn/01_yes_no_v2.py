show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
show_instructions = input("Have you played this game before?").lower()

# If they say yes output 'programme continue'
# If they say no, output 'display instructions'
# If the answer is invalid, print an error.