# Import your Game class
from game import Game
from phrase import Phrase


phrase = Phrase()
game = Game()


phrase = Phrase('Life is like a box of chocolates')
print(phrase.phrase)


# Create your Dunder Main statement.
if __name__ == "__main__":
    game = Game()
    phrase = Phrase()
# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
