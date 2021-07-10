# Create your Phrase class logic here.

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def display(self, guesses):
        for letter in self.phrase:
            if letter == ' ':
                print(' ', end = ' ')
            elif letter in guesses:
                print(f'{letter}', end = " ")
            else:
                print('_', end = ' ')