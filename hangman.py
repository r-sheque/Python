### Do not modify the code at the top of this file! ###
import random

def get_random_word():
	"""This function retrieves a random word from a file called 'words.txt'"""
	with open("./words.txt", "r") as file:
		words = [line.strip() for line in file]
	return random.choice(words)
	
# This is a list containing ascii art for the hangman character
stages = [
r'''
  _____
 |/    |
 | 
 | 
 | 
_|___
''',
r'''
  _____
 |/    |
 |     O
 |    
 |    
_|___
''',
r'''
  _____
 |/    |
 |     O
 |    /|
 |    
_|___
''',
r'''
  _____
 |/    |
 |     O
 |    /|\
 |    
_|___
''',
r'''
  _____
 |/    |
 |     O
 |    /|\
 |    / 
_|___
''',
r'''
  _____
 |/    |
 |     O
 |    /|\
 |    / \
_|___
'''
]
"""
### The global variables you might want to use in this program! ###
# A string that contains the random word we are guessing
# A list that keeps track of which letters the user guessed!
# A list to keep track of which letters were guessed that are right.
# An integer that keeps track of how many mistakes the user has made.

### I need the functions here! ###
"""

var_word = get_random_word()
var_guessed_letters = []
var_correct_letters = []
var_mistakes = 0 

def print_player(mistakes):
	print(stages[mistakes])
	
	if mistakes == 5: 
		return True 
	else: 
		return False

def check_letter(word_or_list, letter):
	for item in word_or_list:
		if item == letter:
			return True
		return False

def get_letter(guessed_letters):
	while True:
		var_letter = input("Guess a letter:").lower() 
		
		if len(var_letter) == 1:
			if not check_letter(guessed_letters, var_letter):
				return var_letter
		print("Please enter one letter that you have not already guessed")
 
def print_word(word, correct_letters):
	for letter in word:
		if check_letter(correct_letters, letter):
			print(letter, end="")
		else:
			print("_", end="")
			
	print()
	print("Guessed letters:", var_guessed_letters)
	
def did_player_win(word, correct_letters):
	for letter in word:
		if not check_letter(correct_letters, letter):
			return False
	return True 	
	
def guess_letter(letter, word, guessed_letters, correct_letters):
	global var_mistakes 
	
	guessed_letters.append(letter)
	
	if check_letter(word, letter):
		correct_letters.append(letter)
	else: 
		var_mistakes += 1 
		print("You are wrong!")
		
def play_game():
	global var_word
	global var_guessed_letters 
	global var_correct_letters 
	global var_mistakes 
	
	var_word = get_random_word()
	var_guessed_letters = []
	var_correct_letters = []
	var_mistakes = 0
	
	while True:
		if print_player(var_mistakes):
			print("You lose")
			return
			
		print_word(var_word, var_correct_letters)
		var_letter = get_letter(var_guessed_letters)
		
		guess_letter(
			var_letter,
			var_word,
			var_guessed_letters,
			var_correct_letters
			)
		if did_player_win(var_word, var_correct_letters):
			print("You won!")
			return

play_game()
