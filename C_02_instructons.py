# functions go here

def yes_no(question):...


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ****

Roll the dice and try to win!
    """)


# Main routine

# ask user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program continues")