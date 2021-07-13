# Create your Game class logic in here.
from phrase import Phrase
import random


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
    
    def create_phrases(self):
        list = [
            Phrase("Hello World"),
            Phrase("There is no trying"),
            Phrase("May the force be with you"),
            Phrase("Life is like a box of chocolates"),
            Phrase("You have to see the matrix for yourself")
            ]   
        return list
    
    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrases)
        return self.active_phrase
    
    def welcome(self):
        print(' ' * 6, '--' * 14, end = '\n\n')
        print(' ' * 10, 'Welcome to my game!', end = '\n\n')
        print(' ' * 6, '--' * 14, end = '\n\n\n')
        
    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print('Number missed: ', self.missed, end = '\n\n')
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            self.active_phrase.check_guess(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
            self.active_phrase.check_complete(self.guesses)
        self.game_over()
    
    def get_guess(self):
        guess = str(input("\nGuess a letter. --> "))
        return guess.lower()
    
    def game_over(self):
        if self.missed == 5:
            print('Oh no! You lost.')
        else:
            print('Congratulations! You won the game.')