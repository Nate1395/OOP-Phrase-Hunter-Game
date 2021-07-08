# Import your Game class
from game import Game

def print_phrase(phrase_object):
    print(f'The phrase is: {phrase_object.phrase}')

game = Game()
print_phrase(game.get_random_phrase()) 
print_phrase(game.get_random_phrase()) 
print_phrase(game.get_random_phrase()) 
print_phrase(game.get_random_phrase()) 
print_phrase(game.get_random_phrase())


# Create your Dunder Main statement.
if __name__ == "__main__":
    pass
# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
