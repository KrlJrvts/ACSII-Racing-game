from raceoptions import race_options
from scoreboard import scoreboard

""" Game menu for ASCII Racing game"""


print("___________________________")
print("Welcome to the racing game!")
print("___________________________")

player_option = None

while True:
    print("Please choose:")
    print("1 - New Game")
    print("2 - Scoreboard")
    print("3 - Exit game")
    player_option = input("Answer: ")
    if player_option == "1":
        race_options()
    elif player_option == "2":
        scoreboard()
    elif player_option == "3":
        break
    else:
        print("Please choose option 1, 2 or 3")

print("Than You for playing THE GAME!")
print("WROOM WROOM WROOOOOOOOOOOM!")
