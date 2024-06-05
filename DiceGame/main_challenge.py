'''
challenge
◼️ Non-public Methods
Methods can be non-public too, just like attributes. You just need to add an underscore before their names.

Did you notice that most of the methods in the DiceGame class are only used inside the class?

They can be non-public! Try to make this change in your code and see how it works.

◼️ Use the value Attribute
In the DiceGame class, instead of using variables to store the new values of the dice, try to change the code to work with the value attributes directly.

💡 Tip: In this case, you would not need to return the value from the roll_dice and roll methods and you can access the attribute using dot notation.

◼️ Remove Repetition
In the .show_game_over() method of the DiceGame class, try to write the first three print statements and the last print statement outside the conditional to avoid repeating them. We only need to customize the line that congratulates the winner.

◼️ Roll the Dice
In the DiceGame class, define a new method to roll the dice. Then, call this method from the play_round method.




'''

import random


class Die:
    
    def __init__(self):
        self._value = None
        
    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value


class Player:
    
    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10
        
    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter += 1
        
    def decrement_counter(self):
        self._counter -= 1
    
    
class DiceGame:
    
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        
    def play(self):
        print("==================================")
        print("Welcome to Roll the Dice!!!")
        print("==================================")

        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break
            
    def play_round(self):
        # Welcome the user
        self.print_round_welcome()

        # Roll the dice
        self._player.die.roll()
        self._computer.die.roll()
        
        # Show the values
        self.show_dice(self._player.die.value, self._computer.die.value)
        
        # Determine winner and loser
        if self._player.die.value > self._computer.die.value:
            print("You won the round")
            self.update_counters(winner=self._player, loser=self._computer) 
        elif self._computer.die.value > self._player.die.value:
            print("The computer won this round. Try again.")
            self.update_counters(winner=self._computer, loser=self._player)
        else:
            print("It's a tie!")
        
        # Show counters
        self.show_counters()

    def print_round_welcome(self):
        print("\n------- New Round -------")
        input("Press any key to roll the dice!")
        
    def show_dice(self, player_value, computer_value):
        print(f"Your die:{player_value}")
        print(f"Computer die:{computer_value}\n")
        
    def update_counters(self, winner, loser):
        winner.decrement_counter() # Winner
        loser.increment_counter() # Loser
        
    def show_counters(self):
        print(f"\nYour counter:{self._player.counter}")
        print(f"Computer counter:{self._computer.counter}")
        
    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False
            
    def show_game_over(self, winner):
        print("\n===============================")
        print("GAME OVER")
        if winner.is_computer:
            print("The computer won the game.")
        else:
            print("You won the game! Congratulations!")           
        print("===============================\n")
        
               
            
'''
# Testing Die class
print("Testing Die class")
die = Die()

print(die.value)

die.roll()
print(die.value)

# Testing Player class
print("Testing Player class")
my_die = Die()
my_player = Player(my_die, is_computer=False)

print(my_player.is_computer)

print(my_player.counter)
my_player.increment_counter()
print(my_player.counter)

print(my_die.value)
my_player.roll_die()
print(my_die.value)

print(my_player.die.value)

'''

# Create instances
print("Testing DiceGame class")
player_die = Die()
computer_die = Die()

my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

# Start the game
game.play()

