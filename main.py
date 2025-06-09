from colorama import Fore
from time import clock
from random import randint
import os
from time import sleep
#Opening screen
print(Fore.RED + "This is the Game that will bring your demise.")
print(Fore.RED + "The Game where you dance with death.")
sleep(5)
#I want the playere to be able to read the previous string
os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.RED + "WECLOME PLAYER TO OTRIO\n")
#This is my Grid List
def grid():
    #I am using a 3D list to make it the grid look more like a list, this is also because I need to only use one board making it easier to code
    otrio_grid = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
    return otrio_grid

#Player token list
def reset_tokens(colour):
    #Biggest Token
    big_token = [colour + "0", "0", "0"]
    #Middle sized Token
    medium_token = [colour + "O", "O", "O"]
    #Smallest Token
    small_token = [colour + "o", "o", "o"]

    return big_token, medium_token, small_token

#Rules of the game.
def rules_call():
    print(Fore.BLUE + "These are the rules for otrio"
          ,Fore.GREEN + "\nYou and your opponent have three different tokens:" 
          ,Fore.WHITE + "\n'o' , 'O' and '0'"
          ,Fore.GREEN + "\nThe 'o' token is the smallest of the three tokens it can be overlapped by 'O' and '0' however this token is very effective to map out your strategy.\nThe 'O' token is medium sized it can overlap the 'o' token however it can be overlapped by the'0' token.\nFinally the '0' token is the biggest of the three and can overlap any token."
          ,Fore.MAGENTA + "\nThe board looks like this:\n   1    2    3\nA ' '  ' '  ' '\nB ' '  ' '  ' '\nC ' '  ' '  ' '"
          ,Fore.GREEN + "\nTo put something in the board you put the the number of the row, the letter of the row and the token you want to use \ni.e. 2B0")
    return rules_call

def player_one_opponent(i, row, column, otrio_grid, big_token, small_token, medium_token):
    ai_row = randint(1, 3)
    ai_column = randint(1, 3)

#What is used to play the game
def press_play(otrio_grid, big_token, small_token, medium_token):
    tokens_combined = [big_token, small_token, medium_token]
    choose_your_fight = input("Who do you wish to face:\nPLAYER 1 or PLAYER 2?")
    #Easier AI. I will make it choose a random square to place the token and a random token to use
    if choose_your_fight == "PLAYER 1":
        print(otrio_grid)
        location_of_tile = input("").upper()
        i = 0
        n = 1
        
        column, row, piece = location_of_tile

        #How the player can place a token
        if piece in tokens_combined:
            tokens_combined.remove(piece)
            if row.alpha() == True:
                letter_for_row = ord(row)
                if letter_for_row == 41:
                    i = 0
                elif letter_for_row == 42:
                    i = 1
                elif letter_for_row == 43:
                    i = 2
                if ord(column) == 49 or ord(column) == 50 or ord(column) == 51:
                    if ord(column) == 49:
                        n = 0
                    elif ord(column) == 50:
                        n = 1
                    elif ord(column) == 51:
                        n += 1
                else:
                    print("You truly have failed this battle.")
            else:
                    print("You truly have failed this battle.")
        else:
                    print("You truly have failed this battle.")
    #Player 2. Harder version of Otrio. Will have 3 rounds. First is automatic lose, second is difficult but can still win and final is a timed match.
    elif choose_your_fight == "PLAYER 2":
        print(otrio_grid)
        location_of_tile = input("").upper()
        i = 0
        n = 1
        
        column, row, piece = location_of_tile
        if piece in tokens_combined:
            tokens_combined.remove(piece)
            if row.alpha() == True:
                letter_for_row = ord(row)
                if letter_for_row == 41:
                    i = 0
                elif letter_for_row == 42:
                    i = 1
                elif letter_for_row == 43:
                    i = 2
                if ord(column) == 49 or ord(column) == 50 or ord(column) == 51:
                    if ord(column) == 49:
                        n = 0
                    elif ord(column) == 50:
                        n = 1
                    elif ord(column) == 51:
                        n += 1
                else:
                    print("You have failed my expectations. You are worthless.")
            else:
                    print("You have failed my expectations. You are worthless.")
        else:
                    print("You have failed my expectations. You are worthless.")
    return row, column, piece, i, n

#playing the game. where everything begins
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


#Worthless line... Could be useful for later

        # # we know the piece if valid

        # # so you need to use the row to decide the i index

        # # use the column to decide the n index



        # # put the piece in the grid at position [i][n]
        #     i = 
        #     n = 


        #     otrio_grid[i][n] = "o"

        #     if piece == tokens_combined:
                
                    
        #                 otrio_grid[i][n] = 'o'
        #             elif column == '2':
        #                 n += 1
        #                 otrio-grid[i][n] = 'o'
        #             elif column == '3':
        #                 n += 2
        #                 otrio_grid[i][n] = 'o'
        #             else:
        #                 print("You truly have failed this battle.")
        #         elif row == 'B':
        #             if column == '1':
        #                 i += 1
        #                 otrio_grid[i][n] = 'o'
        #             elif column == '2':
        #                 i += 2
        #                 n += 1
        #                 otrio-grid[i][n] = 'o'
        #             elif column == '3':
        #                 n += 2
        #                 i += 3
        #                 otrio_grid[i][n] = 'o'
        #             else:
        #                 print("You truly have failed this battle.")
        #         elif row == 'C':
        #             if column == '3':
        #                 i += 1
        #                 otrio_grid[i][n] = 'o'
        #             elif column == '2':
        #                 i += 2
        #                 n += 1
        #                 otrio-grid[i][n] = 'o'
        #             elif column == '3':
        #                 n += 2
        #                 i += 3
        #                 otrio_grid[i][n] = 'o'

                # if 'o' in location_of_tile:
        #     if piece == tokens_combined:
        #         if row == 'A':
        #             if column == '1':
        #                 otrio_grid[i][n] = 'o'
        #             elif column == '2':
        #                 n += 1
        #                 otrio-grid[i][n] = 'o'
        #             elif column == '3':
        #                 n += 2
        #                 otrio_grid[i][n] = 'o'
        #             else:
        #                 print("You truly have failed this battle.")
        #         elif row == 'B':
        #             if column == '1':
        #                 i += 1
        #                 otrio_grid[i][n] = 'o'
        #             elif column == '2':
        #                 i += 2
        #                 n += 1
        #                 otrio-grid[i][n] = 'o'
        #             elif column == '3':
        #                 n += 2
        #                 i += 3
        #                 otrio_grid[i][n] = 'o'
        #             else:
        #                 print("You truly have failed this battle.")
        #         elif row == 'C':
        #             if column == '3':
        #                 i += 1
        #                 otrio_grid[i][n] = 'o'
        #             elif column == '2':
        #                 i += 2
        #                 n += 1
        #                 otrio-grid[i][n] = 'o'
        #             elif column == '3':
        #                 n += 2
        #                 i += 3
        #                 otrio_grid[i][n] = 'o'
         #           else:
         #               print("You have failed my expectations. You are worthless.")
       # else:
            #print("You truly are not worthy of this.")
#    else:
 #       print(Fore.YELLOW + "Don't make me laugh that is not a number you utter buffoon. ")