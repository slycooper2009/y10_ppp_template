from colorama import Fore
import os
from time import sleep
#I found this online wanted to try it out
#I understand how it works
#Opening screen
print(Fore.RED + "This is the Game that will bring your demise.")
print(Fore.RED + "The Game where you dance with death.")
sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.RED + "WECLOME PLAYER TO OTRIO\n")
#Grid List
def grid():
    otrio_grid = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
    return otrio_grid

#Player token list
def reset_tokens(colour):
    big_token = [colour + "0", "0", "0"]
    medium_token = [colour + "O", "O", "O"]
    small_token = [colour + "o", "o", "o"]

    return big_token, medium_token, small_token

#rules
def rules_call():
    print(Fore.BLUE + "These are the rules for otrio"
          ,Fore.GREEN + "\nYou and your opponent have three different tokens:" 
          ,Fore.WHITE + "\n'o' , 'O' and '0'"
          ,Fore.GREEN + "\nThe 'o' token is the smallest of the three tokens it can be overlapped by 'O' and '0' however this token is very effective to map out your strategy.\nThe 'O' token is medium sized it can overlap the 'o' token however it can be overlapped by the'0' token.\nFinally the '0' token is the biggest of the three and can overlap any token."
          ,Fore.MAGENTA + "\nThe board looks like this:\n   1    2    3\nA ' '  ' '  ' '\nB ' '  ' '  ' '\nC ' '  ' '  ' '"
          ,Fore.GREEN + "\nTo put something in the board you put the the number of the row, the letter of the row and the token you want to use \ni.e. 2B0")
    return rules_call

def press_play(otrio_grid):
    choose_your_fight = input("Who do you wish to face:\nPLAYER 1 or PLAYER 2?")
    if choose_your_fight == "PLAYER 1".lower():  # ALWAYS FALSE
        print(otrio_grid)
        location_of_tile = input("")
        if 'o' in location_of_tile:
            if '1' and 'A'.lower() in location_of_tile:
                otrio_grid.append(1, 'o')
            elif '2' and 'B'.lower() in location_of_tile:
                otrio_grid.append(2, 'o')
            elif '3' and 'B'.lower() in location_of_tile:
                otrio_grid.append(3, 'o')
        elif 'O' in location_of_tile:
            if '1' and 'A'.lower() in location_of_tile:
                otrio_grid.append(4, 'o')
            elif '2' and 'B'.lower() in location_of_tile:
                otrio_grid.append(5, 'o')
            elif '3' and 'B'.lower() in location_of_tile:
                otrio_grid.append(6, 'o')
        elif '0' in location_of_tile:
            if '1' and 'A'.lower() in location_of_tile:
                otrio_grid.append(7, 'o')
            elif '2' and 'B'.lower() in location_of_tile:
                otrio_grid.append(8, 'o')
            elif '3' and 'B'.lower() in location_of_tile:
                otrio_grid.append(9, 'o')
        else:
            print("You truly have failed this battle.")
    elif choose_your_fight == "PLAYER 2".lower():
        print(otrio_grid)
        location_of_tile = input("")
        if 'o' in location_of_tile:
            if '1' and 'A'.lower() in location_of_tile:
                otrio_grid.append(1, 'o')
            elif '2' and 'B'.lower() in location_of_tile:
                otrio_grid.append(2, 'o')
            elif '3' and 'B'.lower() in location_of_tile:
                otrio_grid.append(3, 'o')
        elif 'O' in location_of_tile:
            if '1' and 'A'.lower() in location_of_tile:
                otrio_grid.append(4, 'o')
            elif '2' and 'B'.lower() in location_of_tile:
                otrio_grid.append(5, 'o')
            elif '3' and 'B'.lower() in location_of_tile:
                otrio_grid.append(6, 'o')
        elif '0' in location_of_tile:
            if '1' and 'A'.lower() in location_of_tile:
                otrio_grid.append(7, 'o')
            elif '2' and 'B'.lower() in location_of_tile:
                otrio_grid.append(8, 'o')
            elif '3' and 'B'.lower() in location_of_tile:
                otrio_grid.append(9, 'o')
        else:
            print("You truly are not worthy of this.")
    else:
        print(Fore.YELLOW + "Don't make me laugh that is not a number you utter buffoon. ")

#play
def press_start(otrio_grid):

    game_end = False
    while game_end != True:
        print(Fore.MAGENTA + "Type what you want to do.")
        what_u_want_to_do = input(Fore.BLUE + "(Press Play)\n(Rules)\n(I Give Up)\n")
        if what_u_want_to_do == "(Press Play)":
            choose_your_fight = input("Who do you wish to face:\nPLAYER 1 or PLAYER 2?")
            if choose_your_fight == "PLAYER 1".lower():
                print(otrio_grid)
            elif choose_your_fight == "PLAYER 2".lower():
                print(otrio_grid)
            else:
                print(Fore.YELLOW + "Don't make me laugh that is not a number you utter buffoon. ")
        elif what_u_want_to_do == "(Rules)":
            os.system('cls')
            rules_call()
        elif what_u_want_to_do == "(I Give Up)":
            game_end = True

press_start()


big_token, medium_token, small_token = reset_tokens(Fore.BLUE)
