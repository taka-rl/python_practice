import random
from player import Player
from board import Board


class TicTacToeGame:
    def start(self):
        print("***********************")
        print(" Welcome to Tic-Tac-Toe ")
        print("***********************")

        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()
        while True:  # Game
            # set the play order
            if random.randint(0, 1):
                # player first
                self.game(board, [player, computer], player=True)
            else:
                # computer first
                self.game(board, [computer, player], player=False)
            player_again = input("Would you like to play again? Enter X for Yes or 0 for No: ").upper()

            if player_again == "0":
                print("Bye! Come back soon!")
                break
            elif player_again == "X":
                self.start_new_round(board)
            else:
                print("Your input was not valid but I will assume that you want to play again!")

    @staticmethod
    def game(board, players, player):
        player1, player2 = players
        if player:
            print("----- You are player1 -----")
        else:
            print("----- You are player2 -----")

        while True:  # Round
            while True:
                player1_move = player1.get_move()
                if board.submit_move(player1, player1_move):
                    break
            board.print_board()

            if board.check_is_game_over(player1, player1_move):
                print("Awesome. player1 won the game!")
                break
            elif board.check_is_tie():
                print("It's a tie! Try again!")
                break
            else:
                while True:
                    player2_move = player2.get_move()
                    if board.submit_move(player2, player2_move):
                        break
                board.print_board()

                if board.check_is_game_over(player2, player2_move):
                    print("Awesome. player2 won the game!")
                    break
                elif board.check_is_tie():
                    print("It's a tie! Try again!")
                    break

    @staticmethod
    def start_new_round(board):
        print("***************")
        print(" New Round ")
        print("***************")
        board.reset_board()
        board.print_board()


if __name__ == "__main__":
    game = TicTacToeGame()
    game.start()
