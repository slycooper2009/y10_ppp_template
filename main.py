from colorama import Fore
#Opening screen
player_1_intro = print(Fore.RED + "This is the Game that will bring your demise.")
player_2_intro = print(Fore.RED + "The Game where you dance with death.")
open_screen = print(Fore.RED + "WECLOME PLAYER TO OTRIO")
#Grid List
otrio_grid = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]
print(otrio_grid)

#Player token list
def reset_tokens(colour):
    big_token = [colour + "0", "0", "0"]
    mesium_token = [colour + "O", "O", "O"]
    small_token = [colour + "o", "o", "o"]

    return big_token, mesium_token, small_token

print(reset_tokens)
# #bot token
# def bot_reset_tokens():
#     bot_big_token = ["0", "0", "0"]
#     bot_mesium_token = ["O", "O", "O"]
#     bot_small_token = ["o", "o", "o"]

#rules
def rules_call():
    print("")

#play
def press_start():
    choose_your_fight = input("Who do you wish to face:\nPLAYER 1 or PLAYER 2?")
    if choose_your_fight == "PLAYER 1".lower:
        print(otrio_grid)
    elif choose_your_fight == "PLAYER 2".lower:
        print(otrio_grid)
    else:
        print("")



big_token, mesium_token, small_token = reset_tokens(Fore.BLUE)
