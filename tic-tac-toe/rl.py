# https://chat.openai.com/share/6075678c-eb0d-4420-87cb-81bdd79841ac

import random

from move import Move
from player import Player
from board import Board

class QLearningAgent:
    def __init__(self, epsilon=0.1, alpha=0.3, gamma=0.9):
        self.q_values = {}  # Q-values dictionary
        self.epsilon = epsilon  # Exploration rate
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor

    def get_q_value(self, state, action):
        return self.q_values.get((state, action), 0.0)

    def update_q_value(self, state, action, value):
        current_q = self.get_q_value(state, action)
        new_q = (1 - self.alpha) * current_q + self.alpha * value
        self.q_values[(state, action)] = new_q

    def choose_action(self, state, possible_actions):
        if random.random() < self.epsilon:
            return random.choice(possible_actions)  # Exploration
        else:
            max_q_value = max(self.get_q_value(state, action) for action in possible_actions)
            best_actions = [action for action in possible_actions if self.get_q_value(state, action) == max_q_value]
            return random.choice(best_actions)  # Exploitation

    def train(self, state, action, reward, next_state):
        max_next_q = max(self.get_q_value(next_state, next_action) for next_action in range(9))
        target = reward + self.gamma * max_next_q
        self.update_q_value(state, action, target)

class RLGame:
    def __init__(self):
        self.q_agent = QLearningAgent()
        self.board = Board()
        self.player = Player()
        self.computer = Player(False)

    def start(self):
        print("***********************")
        print(" Welcome to Tic-Tac-Toe ")
        print("***********************")

        self.board.print_board()

        while True:  # Game
            while True:  # Round
                player_move = self.player.get_move()
                self.board.submit_move(self.player, player_move)
                self.board.print_board()

                if self.board.check_is_game_over(self.player, player_move):
                    print("Awesome. You won the game!")
                    break
                elif self.board.check_is_tie():
                    print("It's a tie! Try again!")
                    break
                else:
                    computer_move = self.computer.get_move()
                    self.board.submit_move(self.computer, computer_move)
                    self.board.print_board()

                    if self.board.check_is_game_over(self.computer, computer_move):
                        print("Oops, the computer won. Try again!")
                        break
                    elif self.board.check_is_tie():
                        print("It's a tie! Try again!")
                        break

#                self.q_agent.train(self.board.get_state(), player_move.value, 0, self.board.get_state())
                self.q_agent.train(self.board.get_state(self.player), player_move.value, 0, self.board.get_state(self.computer))

            player_again = input("Would you like to play again? Enter X for Yes or 0 for No: ").upper()

            if player_again == "0":
                print("Bye! Come back soon!")
                break
            elif player_again == "X":
                self.start_new_round()
            else:
                print("Your input was not valid but I will assume that you want to play again!")

    def start_new_round(self):
        print("***************")
        print(" New Round ")
        print("***************")
        self.board.reset_board()
        self.board.print_board()

if __name__ == "__main__":
    game = RLGame()
    game.start()
