# Create your Game class logic in here.
from phrase import Phrase
import random


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = None
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