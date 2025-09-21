from color_scheme import *
import time
import random

# custom length error exception
class LengthError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.code})"

class Game:
    # global variables chance and count
    def __init__(self):
        self.chance = 6
        self.score = 0

    # function to check length of the word entered by the user
    def checkLen(self, word):
        return len(word) == 5 
    

    # function to select a random word from the list of words
    def WordToGuess(self):
        with open("words.txt", 'r') as f:
            words = f.read().splitlines()
        return random.choice(words).upper()

    # function to check if the word entered by the user is correct or not
    def checkGuess(self, word, toGuess):
        if word == toGuess: 
            return 1
        else:
            self.chance -= 1 # decrease chance by 1
            return 0

    # main game function
    def game(self):
        word = self.WordToGuess() # word to be guessed
        print("\tWELCOME TO WORDLE\t")
        time.sleep(2) # wait for 2 seconds, simulating loading time
        option = input("Want to read rules (y/n): ")
        if option.lower() == 'y':
            with open("rules.txt",'r') as f: # reading rules from rules.txt file
                rules = f.read()
            print(rules)
        print("Enter your guess: ")
        while self.chance > 0:
            try:
                guess = input().upper()
                if not self.checkLen(guess): # length condition
                    raise LengthError("Invalid length of the word... Length should be 5", 100)
                print(display_word(guess, word)) # using display_word function from color_scheme.py to display colored output
                if self.checkGuess(guess, word) == 1:
                    self.score = self.chance * 100
                    print(f"You won! \nYour score: {self.score}")
                    break
                else:
                    print("Wrong guess...")
                    print(f"Chances remaining: {self.chance}")
            except LengthError as e:
                print(e)
        else: # if chances are over
            print("Sorry, no more chances left...")
            print(f"The word was: {word}")

if __name__ == '__main__':
    g = Game()

    g.game()
