# Xubo Zhu
# ITP 115
# Assignment 5
# 2/19/2017
# Description: Tic Tac Toe


import TicTacToeHelper

board_list = [0,1,2,3,4,5,6,7,8]


# define isValidMove:
# input: a list representing the board
#        an integer representing the spot of the board
# return: true or false
def isValidMove(board_list, spot):
    valid = True
    if board_list[spot] == "x" or board_list[spot] == "o":
        valid = False
    else:
        valid = True
    return valid


#define updateBoard:
# input: the board_list above
#          the spot above
#          a string representing the player's letter
# return: none
def updateBoard(board_list, spot, player_letter):
    board_list[spot] = player_letter


# define playGame:
# input: none
# return: none
def playGame():
    move_counter = 1
    result = "n"            #to check for whether the game has finished or not; if result is n, then the program goes on

    print("Welcome to tic tac toe!")

    while result == "n":
        if move_counter % 2 == 1:       #this works as a variable to determine whether it is x's turn or o's turn.
            player_letter = "x"

            TicTacToeHelper.printUglyBoard(board_list)
            spot = int(input("Player x, pick a spot:"))
            while spot not in board_list:           # Error check. To make sure the user enter an open spot and in range 0~8.
                spot = int(input("""Invalide move. Please try again.
Player x, pick a spot:"""))

            valid = isValidMove(board_list, spot)

            updateBoard(board_list, spot, player_letter)

            result = TicTacToeHelper.checkForWinner(board_list, move_counter)

            move_counter = move_counter + 1

        elif move_counter % 2 == 0:                                                        # O's turn.
            player_letter = "o"

            TicTacToeHelper.printUglyBoard(board_list)
            spot = int(input("Player o, pick a spot:"))
            while spot not in board_list:
                spot = int(input("""Invalid move, please try again.
Player o, pick a spot:"""))

            valid = isValidMove(board_list, spot)

            updateBoard(board_list, spot, player_letter)

            result = TicTacToeHelper.checkForWinner(board_list, move_counter)

            move_counter += 1

    if result =="x":
        print("Game over!"
              "\nPlayer x is the winner!")

    elif result =="o":
        print("Game over!"
              "\nPlayer o is the winner!")

    elif result == "s":
        print("Game over!"
              "\nNobody wins! Stalemate reached!")


# define main:
# input: none.
# return: none.
def main():
    again = "y"
    while again.lower() == "y":
        playGame()
        again = input("Would you like to play another round? (y/n)")
        board_list[0] = 0                                               # These are used to refresh the board.
        board_list[1] = 1
        board_list[2] = 2
        board_list[3] = 3
        board_list[4] = 4
        board_list[5] = 5
        board_list[6] = 6
        board_list[7] = 7
        board_list[8] = 8
    if again.lower() == "n":
        print("Goodbye!")
main()












