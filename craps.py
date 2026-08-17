import random
import sys

ans = input("To start the game write 'yes' to quit write 'no' \n ")
if ans.lower() == "no":
    sys.exit()
else:
    print("So,let's start the game!")

#to continue with or without construction

cont = input("Welcome! If you want the game instructions write 'yes',otherwise write 'no'")

if cont.lower() == "yes":
    print("Here are the rules of the game: " \
    "The player should roll two dice. If the sum of both of them is 7 or 11 the player wins. " \
    "If the sum is 2, 3 or 12 (craps) the casino wins. If during the first roll the sum is 4, 5, 6, 8, 9 or 10, that number becomes the “goal” number. " \
    "To win, the player should roll the dice till they roll the goal number again. If the player rolls a 7 before rolling the goal number, they lose.")

elif cont.lower() == "no":
    print("Best luck!")

   
