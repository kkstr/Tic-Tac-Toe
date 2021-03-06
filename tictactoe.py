def main():
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    print_board(board)
    game_on = True
    turn = "X"
    counter = 0
    while game_on:
        if turn == "X":
            move = input("\nX's turn: ")
            if move == "q":
                break
            elif move == "r":
                board = ["-", "-", "-",
                         "-", "-", "-",
                         "-", "-", "-"]
                print_board(board)
                turn = "X"
                counter = 0
            else:
                try:
                    move = int(move)
                    move_final = move - 1
                    if move_final < 0 or move_final  > 8:
                        print("That is an invalid move. Try again.")
                    elif board[move_final] != "-":
                        print("That space is already taken. Try again.")
                    else:
                        board[move_final] = "X"
                        counter += 1
                except ValueError:
                    print("That is an invalid move. Try again.")
        else:
            move = input("\nO's turn: ")
            if move == "q":
                break
            elif move == "r":
                board = ["-", "-", "-",
                         "-", "-", "-",
                         "-", "-", "-"]
                print_board(board)
                turn = "O"
                counter = 0
            else:
                try:
                    move = int(move)
                    move_final = move - 1
                    if move_final < 0 or move_final > 8:
                        print("That is an invalid move. Try again.")
                    elif board[move_final] != "-":
                        print("That space is already taken. Try again.")
                    else:
                        board[move_final] = "O"
                        counter += 1
                except ValueError:
                    print("That is an invalid move. Try again.")
        print_board(board)
        if counter == 9:
            print("\nThe game is a draw.")
            break
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    print("\nThanks for playing!")


def print_board(board):
    print("\n" + board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 11)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 11)
    print(board[6] + " | " + board[7] + " | " + board[8])


if __name__ == "__main__":
    main()


#!/usr/bin/env python3