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

def press_play(otrio_grid, big_token, small_token, medium_token):
    tokens_combined = [big_token, small_token, medium_token]
    choose_your_fight = input("Who do you wish to face:\nPLAYER 1 or PLAYER 2?")
    if choose_your_fight == "PLAYER 1":  # ALWAYS FALSE
        print(otrio_grid)
        location_of_tile = input("")
        
        i = 0
        n = 1
        for b in range(3):    
            column, row, piece = location_of_tile
            if piece == tokens_combined:
                if row == 'A':
                    if column == '1':
                        otrio_grid[i][n] = 'o'
                    elif column == '2':
                        n += 1
                        otrio-grid[i][n] = 'o'
                    elif column == '3':
                        n += 2
                        otrio_grid[i][n] = 'o'
                    else:
                        print("You truly have failed this battle.")
                elif row == 'B':
                    if column == '1':
                        i += 1
                        otrio_grid[i][n] = 'o'
                    elif column == '2':
                        i += 2
                        n += 1
                        otrio-grid[i][n] = 'o'
                    elif column == '3':
                        n += 2
                        i += 3
                        otrio_grid[i][n] = 'o'
                    else:
                        print("You truly have failed this battle.")
                elif row == 'C':
                    if column == '3':
                        i += 1
                        otrio_grid[i][n] = 'o'
                    elif column == '2':
                        i += 2
                        n += 1
                        otrio-grid[i][n] = 'o'
                    elif column == '3':
                        n += 2
                        i += 3
                        otrio_grid[i][n] = 'o'
                    else:
                        print("You truly have failed this battle.")
                    
            else:
                print("You truly have failed this battle.")
    elif choose_your_fight == "PLAYER 2":
        print(otrio_grid)
        location_of_tile = input("").upper()
        #
        if 'o' in location_of_tile:
            
            if '1' in location_of_tile and 'a' in location_of_tile:
                otrio_grid.insert(1, 'o')
            elif '2' and 'B' in location_of_tile:
                otrio_grid.insert(2, 'o')
            elif '3' and 'C' in location_of_tile:
                otrio_grid.insert(3, 'o')
        elif 'O' in location_of_tile:
            if '1' and 'A' in location_of_tile:
                otrio_grid.insert(4, 'o')
            elif '2' and 'B' in location_of_tile:
                otrio_grid.insert(5, 'o')
            elif '3' and 'C' in location_of_tile:
                otrio_grid.insert(6, 'o')
        elif '0' in location_of_tile:
            if '1' and 'A' in location_of_tile:
                otrio_grid.insert(7, 'o')
            elif '2' and 'B' in location_of_tile:
                otrio_grid.insert(8, 'o')
            elif '3' and 'C' in location_of_tile:
                otrio_grid.insert(9, 'o')
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
            pass
        elif what_u_want_to_do == "(Rules)":
            os.system('cls')
            rules_call()
        elif what_u_want_to_do == "(I Give Up)":
            game_end = True

press_start()


big_token, medium_token, small_token = reset_tokens(Fore.BLUE)
