import random


def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    # Roll the dice for the user and note if they get a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total} ")

    return total, double


def make_statement(statement, decoration):
    """Adds emoji / additional characters to the start and end of the headings"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")

# Main starts here...

# At the start of the game, the computer / user score are both zero
comp_score = 0
user_score = 0

game_goal = int(input("Game Goal: "))     # should be a function call!

# Play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    # start of  round loop
    # For testing purposes, ask the user what the points for the user / computer were
    # Roll the dice fpr the user and note if they got a double
    initial_user = initial_points("User")
    initial_comp = initial_points("Comp")

    # Retrieve user points (first item returned from function)
    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    # Let the user know if they qualify for the double points
    if double_user == "yes":
        print("Great news - if you win, you will earn double points!")

    # assume user goes first...
    first = "user"
    second = "Computer"
    player_1_points = user_points
    player_2_points = comp_points

    # if user has fewer points, they start the game
    if user_points < comp_points:
        print("You start because your initial roll was less than the computer\n")

    # if the user and computer roll equal points, the user is player 1...
    elif user_points == comp_points:
        print("The initial rolls were the same, the user starts!")

    # if the computer has fewer points, switch the computer to 'player 1'
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    # loop until we have a winner...
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("Press <enter> to continue this round\n")

        # first person rolls the die and score is updated
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points")

        # if the first person's score is over 13, end the round
        if player_1_points >= 13:
            break

        # second person rolls the die (and score is updated)
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

        print(f"{first}: {player_1_points} | {second} {player_2_points}")

    # end of round

    # associate player points with either the user or the computer
    user_points = player_1_points
    comp_points = player_2_points

    # switch the user and computer points if the computer went first
    if first == "Computer":
        user_points, comp_points = comp_points, user_points

    # work out who won...
    if user_points > comp_points:
        winner = "user"
        loser = "Computer"
        comp_points = 0
    else:
        winner = "computer"
        loser = "user"
        user_points = 0

    round_feedback = f"The {winner} won."

    # double user points if eligible
    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    # Output round results
    make_statement("Round Results", "=")
    print(f"User Points: {user_points} | Computer Points: {comp_points}")
    print(round_feedback)
    print()

    # Outside rounds loop - Update score with round points, only add points to the score of the
    comp_score += comp_points
    user_score += user_points

    # show overall scores (add this to rounds loop)
    print("*** Game Update ***")  # replace with statement generator
    print(f"User Score: {user_score} | Computer Score {comp_score}")


# end of entire game, output final results
print()
if user_score > comp_score:
    print("The user won")   # replace this with statement generator call
else:
    print("The computer won")
