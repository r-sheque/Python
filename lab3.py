import random
options = [ "rock", "paper", "scissors" ]
random_choice = random.choice(options) 

x = input("rock, paper, or scissors?:").lower()

if x == random_choice: 
	print("It's a tie!")	
elif x == "scissors":
	if random_choice == "paper":
		print("You won!")
	else:
		print("Darn!")			
elif x == "paper":
	if random_choice == "rock":
		print("You won!") 
	else:
		print("Darn!")
elif x == "rock":
	if random_choice == "scissors":
		print("You won!")
	else:
		print("Darn!")
				

else:
	print("That wasn't rock, paper, or scissors, cheater!")

print("Computer input:",random_choice)
