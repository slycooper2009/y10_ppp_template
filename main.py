from colorama import Fore
#from time import clock
from random import randint, choice
import os
from time import sleep
#Opening screen
print(Fore.RED + "This is the Game that will bring your demise.")
print(Fore.RED + "The Game where you dance with death.")
sleep(5)
#I want the playere to be able to read the previous string
os.system('cls' if os.name == 'nt' else 'clear')
#This is my Grid List
otrio_inserts = [['','',''],['','',''],['','','']]



def grid():
    #I am using a 3D list to make it the grid look more like a board, this is also because I need to only use one board making it easier to code
    otrio_grid = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
    return otrio_grid

#Player token list
def reset_tokens():
    #Biggest Token
    big_token = ["0", "0", "0"]
    #Middle sized Token
    medium_token = ["O", "O", "O"]
    #Smallest Token
    small_token = ["o", "o", "o"]

    return big_token, medium_token, small_token

#player 1 ai tokens
def ai_tokens():
    #Biggest Token
    ai_big_token = ["0", "0", "0"]
    #Middle sized Token
    ai_medium_token = ["O", "O", "O"]
    #Smallest Token
    ai_small_token = ["o", "o", "o"]

    return ai_big_token, ai_medium_token, ai_small_token

#Rules of the game.
def rules_call():
    print(Fore.BLUE + "These are the rules for otrio"
          ,Fore.GREEN + "\nYou and your opponent have three different tokens:" 
          ,Fore.WHITE + "\n'o' , 'O' and '0'"
          ,Fore.GREEN + "\nThe 'o' token is the smallest of the three tokens it can be overlapped by 'O' and '0' however this token is very effective to map out your strategy.\nThe 'O' token is medium sized it can overlap the 'o' token however it can be overlapped by the'0' token.\nFinally the '0' token is the biggest of the three and can overlap any token."
          ,Fore.MAGENTA + "\nThe board looks like this:\n[' ',  ' ' , ' ']\n[' ', ' ', ' ']\n[' ', ' ', ' ']"
          ,Fore.GREEN + "\nTo put something in the board you put the the number of the column, the letter of the row and the token you want to use \ni.e. 2B0\n\nit will then be displayed as:\n[' ',  ' ' , ' ']\n[' ', '0', ' ']\n[' ', ' ', ' ']"
          ,Fore.CYAN + "\nTo select (Press Play) type into the terminal P\nIf you want to select (Rules) type into the terminal R\nIf you want to select (I Give Up) type into the terminal Q\nHowever if you wish to waste my time with nothing then I will just disqualify you.\nTo exit Rules press Q\n\nI wish you an unpleasant game! Bad Luck!")
    exit_rules = input("")
    if exit_rules == "Q":
        os.system('cls' if os.name == 'nt' else 'clear')
        return rules_call
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welp... I gues your stuck here now. Bye!")
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        while exit_rules != "Q":
            print("")

def token_order(i, n, otrio_grid):
    #If there is already the biggest piece then tell the player to do it again
    pass

def player_one_opponent(i,n, otrio_grid, ai_big_token, ai_small_token, ai_medium_token):
    try_again = False
    while try_again == False:
        ai_row = randint(41, 43)
        num = 0
        ai_column = randint(65, 67)
        ai_tokens_combined = [ai_big_token[num], ai_small_token[num], ai_medium_token[num]]
        ai_piece = choice(ai_tokens_combined)
        ai_i = 0
        ai_n = 0
        if ai_piece in ai_tokens_combined:
            ai_tokens_combined.remove(ai_piece)
            letter_for_row = ai_row
            if letter_for_row == 41:
                ai_i = 0
            elif letter_for_row == 42:
                ai_i = 1
            elif letter_for_row == 43:
                ai_i = 2
            if ai_column == 65 or ai_column == 66 or ai_column == 67:
                if ai_column == 65:
                    ai_n = 0
                elif ai_column == 66:
                    ai_n = 1
                elif ai_column == 67:
                    ai_n += 1
        num += 1
        if ai_i != i:
            if ai_n != n:
                otrio_grid[ai_i][ai_n] = ai_piece
                print("=======")
                for line in otrio_grid:
                    print(line)
                print(ai_i, ai_n)
                print("========")
                otrio_inserts[ai_i][ai_n] = "Ai 1"
                try_again = True


def opponent_two_horrible(i, n, otrio_grid, ai_big_token, ai_small_token, ai_medium_token):
    try_again = False
    while try_again == False:
        ai_row = randint(41, 43)
        num = 0
        ai_column = randint(65, 67)
        ai_tokens_combined = [ai_big_token[num], ai_small_token[num], ai_medium_token[num]]
        ai_piece = choice(ai_tokens_combined)
        print("======")
        print(ai_tokens_combined)
        print("======")
        ai_i = 0
        ai_n = 0
        if ai_piece in ai_tokens_combined:
            ai_tokens_combined.remove(ai_piece)
            letter_for_row = ai_row
            if letter_for_row == 41:
                ai_i = 0
            elif letter_for_row == 42:
                ai_i = 1
            elif letter_for_row == 43:
                ai_i = 2
            if ai_column == 65 or ai_column == 66 or ai_column == 67:
                if ai_column == 65:
                    ai_n = 0
                elif ai_column == 66:
                    ai_n = 1
                elif ai_column == 67:
                    ai_n += 1
        num += 1
        if ai_i != i:
            if ai_n != n:
                otrio_grid[i][n] = ai_piece
                print("=======")
                for line in otrio_grid:
                    print(line)
                try_again = True


#What is used to play the game
def press_play(big_token, small_token, medium_token, otrio_grid):
    #print(big_token)
    tokens_combined = big_token + small_token + medium_token
    
    # Making the player grid equal otrio grid
    player_otrio_grid = otrio_grid
    choose_your_fight = input("Who do you wish to face: \nPLAYER 1 or PLAYER 2? ")
    #Easier AI. I will make it choose a random square to place the token and a random token to use
    if choose_your_fight == "PLAYER 1":
        for line in grid():
            print(line)
        location_of_tile = input("")
        i = 0
        n = 1

        column, row, piece = location_of_tile
        
        #How the player can place a token
        if piece in tokens_combined:
            #print("Y")
            tokens_combined.remove(piece)
            #print("Y")
            if row == "A":
                i = 0
            elif row == "B":
                i = 1
            elif row == "C":
                i = 2
            if ord(column) == 49 or ord(column) == 50 or ord(column) == 51:
                if ord(column) == 49:
                    n = 0
                elif ord(column) == 50:
                    n = 1
                elif ord(column) == 51:
                    n = 2
                else:
                    print("1You truly have failed this battle.")
            else:
                print("2You truly have failed this battle.")
        else:
            print("3You truly have failed this battle.")
        player_otrio_grid[i][n] = piece
        otrio_inserts[i][n] = "Player"
        for line in player_otrio_grid:
            print(line)
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
                if ord(column) == 65 or ord(column) == 66 or ord(column) == 67:
                    if ord(column) == 65:
                        n = 0
                    elif ord(column) == 66:
                        n = 1
                    elif ord(column) == 67:
                        n += 1
                else:
                    print("You have failed my expectations. You are worthless.")
            else:
                    print("You have failed my expectations. You are worthless.")
        else:
                    print("You have failed my expectations. You are worthless.")
    else:
        print("Seems you are not even worthy of begining.")
    if choose_your_fight == "PLAYER 1" or choose_your_fight == "PLAYER 2":
        return row, column, piece, i, n, otrio_grid, player_otrio_grid
    else:
        return otrio_grid

def winner_winner_chicken_dinner(otrio_inserts):
    for i in range(3):
        #check if they are small tokens
        #check medium tokens
        #check big tokens
        #check if they are the players or the Ai's tokens 
        pass

#playing the game. where everything begins
def press_start():
    game_end = False
    while game_end != True:
        print(Fore.RED + "WECLOME PLAYER TO OTRIO\n")
        print(Fore.MAGENTA + "Type what you want to do.")
        what_u_want_to_do = input(Fore.BLUE + "P = (Press Play)\nR = (Rules)\nQ = (I Give Up)\n")
        if what_u_want_to_do == "P":
            os.system('cls' if os.name == 'nt' else 'clear')
            big_token, small_token, medium_token = reset_tokens()
            otrio_grid = grid()
            row, column, piece, i, n, otrio_grid, player_otrio_grid = press_play(big_token, small_token, medium_token, otrio_grid)
            token_order(i, n, otrio_grid)
            ai_big_token, ai_medium_token, ai_small_token = ai_tokens()
            player_one_opponent(i,n, otrio_grid, ai_big_token, ai_small_token, ai_medium_token)
        elif what_u_want_to_do == "R":
            os.system('cls' if os.name == 'nt' else 'clear')
            rules_call()
        elif what_u_want_to_do == "Q":
            game_end = True
        else:
            print("Seems you have failed simple instructions. Well then... Goodbye!")
            sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            game_end = True

press_start()







#Worthless line... Could be useful for later

# def my_function():
     
#      return x, y


# def my_other_function(result1, result2):
#      return answer

# #calling a function
# result1, result2 = my_function()
# new_result = my_other_function(result1, result2)


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
    # try_again = False
    #while try_again == False:
     #  num = 0
      #  ai_column = randint(65, 67)
       # ai_tokens_combined = [ai_big_token[num], ai_small_token[num], ai_medium_token[num]]
#        ai_piece = choice(ai_tokens_combined)
 #       ai_i = 0
  #      ai_n = 0
   #     if ai_piece in ai_tokens_combined:
    #        ai_tokens_combined.remove(ai_piece)
     #       letter_for_row = ai_row
      #      if letter_for_row == 41:
       #         ai_i = 0
        #    elif letter_for_row == 42:
         #       ai_i = 1
          #  elif letter_for_row == 43:
           #     ai_i = 2
            #if ai_column == 65 or ai_column == 66 or ai_column == 67:
             #   if ai_column == 65:
              #      ai_n = 0
               # elif ai_column == 66:
                #    ai_n = 1
                #elif ai_column == 67:
                 #   ai_n += 1
 #       num += 1
  #      if ai_i != i:
   #         if ai_n != n:
    #            otrio_grid[ai_i][ai_n] = ai_piece
     #           print("=======")
      #          for line in otrio_grid:
       #             print(line)
        #        print(ai_i, ai_n)
         #       print("========")
          #      otrio_inserts[ai_i][ai_n] = "Ai 1"
           #     try_again = True


# def opponent_two_horrible(i, n, otrio_grid, ai_big_token, ai_small_token, ai_medium_token):
#     try_again = False
#     while try_again == False:
#         ai_row = randint(41, 43)
#         num = 0
#         ai_column = randint(65, 67)
#         ai_tokens_combined = [ai_big_token[num], ai_small_token[num], ai_medium_token[num]]
#         ai_piece = choice(ai_tokens_combined)
#         print("======")
#         print(ai_tokens_combined)
#         print("======")
#         ai_i = 0
#         ai_n = 0
#         if ai_piece in ai_tokens_combined:
#             ai_tokens_combined.remove(ai_piece)
#             letter_for_row = ai_row
#             if letter_for_row == 41:
#                 ai_i = 0
#             elif letter_for_row == 42:
#                 ai_i = 1
#             elif letter_for_row == 43:
#                 ai_i = 2
#             if ai_column == 65 or ai_column == 66 or ai_column == 67:
#                 if ai_column == 65:
#                     ai_n = 0
#                 elif ai_column == 66:
#                     ai_n = 1
#                 elif ai_column == 67:
#                     ai_n += 1
#         num += 1
#         if ai_i != i:
#             if ai_n != n:
#                 otrio_grid[i][n] = ai_piece
#                 print("=======")
#                 for line in otrio_grid:
#                     print(line)
#                 try_again = True
#print('in press_start')
            #print(big_token)
# print(otrio_grid)
#         location_of_tile = input("").upper()
#         i = 0
#         n = 1
        
#         column, row, piece = location_of_tile
#         if piece in tokens_combined:
#             tokens_combined.remove(piece)
#             if row.alpha() == True:
#                 letter_for_row = ord(row)
#                 if letter_for_row == 41:
#                     i = 0
#                 elif letter_for_row == 42:
#                     i = 1
#                 elif letter_for_row == 43:
#                     i = 2
#                 if ord(column) == 65 or ord(column) == 66 or ord(column) == 67:
#                     if ord(column) == 65:
#                         n = 0
#                     elif ord(column) == 66:
#                         n = 1
#                     elif ord(column) == 67:
#                         n += 1
#                 else:
#                     print("You have failed my expectations. You are worthless.")
#             else:
#                     print("You have failed my expectations. You are worthless.")
#         else:
#                     print("You have failed my expectations. You are worthless.")
# show_grid = grid()