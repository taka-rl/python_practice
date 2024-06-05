from player import Player
from move import Move
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
        
        # Ask the user if he/she would like to
        # play another round.
        while True: # Game

            # Get move, check tie, check game over
            while True: # Round
                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()
                
                if board.check_is_game_over(player, player_move):
                    print("Awesome. You won the game!")
                    #board.check_is_tie():
                    #print("It's a tie! Try again!")
                    break
                elif board.check_is_tie():
                    print("It's a tie! Try again!")
                    #board.check_is_game_over(player, player_move):
                    #print("Awesome. You won the game!")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()
                    
                    if board.check_is_game_over(computer, computer_move):
                        print("Oops, the computer won. Try again!")
                        break
                    elif board.check_is_tie():
                        print("It's a tie! Try again!")
                        break                                                
                    
            player_again = input("Would you like to play again? Enter X for Yes or 0 for No: ").upper()
            
            if player_again == "0":
                print("Bye! Come back soon!")
                break
            elif player_again == "X":
                self.start_new_round(board)
            else:
                print("Your input was not valid but I will assume that you want to play again!")
    
    def start_new_round(self, board):
        print("***************")
        print(" New Round ")
        print("***************")
        board.reset_board()
        board.print_board()

game = TicTacToeGame()
game.start()
