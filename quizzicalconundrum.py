scores = [ 0 , 0 , 0 , 0 , 0 ]
answer_history = []


print("Question 1: What is your favorite sport?") 
print("A: Basketball")
print("B: Football")
print("C: Soccer")
print("D: Golf")

answer = input("Enter your answer: ").lower()
answer_history.append(answer)

if answer == "a":
	scores[0] +=3 
elif answer == "b":
	scores[1] +=2
elif answer == "c":
	scores[2] +=1
elif answer == "d":
	scores[3] +=0

print('Question 2: Which state has the "best" professional sports?')
print("A: Wisconsin")
print("B: Ohio")
print("C: Michigan")
print("D: Minnesota")
print("E: I don't know much about professional sports")

answer = input("Enter your answer: ").lower()
answer_history.append(answer)

if answer == "a":
	scores[0] +=1 
elif answer == "b":
	scores[1] -=3
elif answer == "c":
	scores[2] +=3
elif answer == "d":
	scores[3] +=1
elif answer == "e":
	scores[4] +=0

print("Question 3: Which is your favorite professional sports league?")
print("A: NHL")
print("B: MLB")
print("C: NFL")
print("D: NBA")
print("E: I don't watch any professional sports")

answer = input("Enter your answer: ").lower()
answer_history.append(answer)

if answer == "a":
	scores[0] +=1 
elif answer == "b":
	scores[1] +=1
elif answer == "c":
	scores[2] +=2
elif answer == "d":
	scores[3] +=3
elif answer == "e":
	scores[4] +=0

print("Question 4: Which is your favorite professional sports team?")
print("A: Detroit Tigers")
print("B: Detroit Pistons")
print("C: Detroit Red Wings")
print("D: Detroit Lions")
print("E: Other")

answer = input("Enter your answer: ").lower()
answer_history.append(answer)

if answer == "a":
	scores[0] +=3 
elif answer == "b":
	scores[1] +=3
elif answer == "c":
	scores[2] +=3
elif answer == "d":
	scores[3] +=3
elif answer == "e":
	scores[4] +=-3
	
print("Question 5: How do you feel about your favorite team's current situation?")
print("A: The Tigers just doing Tigers things")
print("B: The Detroit Pistons never sign what they actually need")
print("C: Who cares the Detroit Red Wings haven't been good in awhile")
print("D: The Detroit Lions always losing in the playoffs")
print("E: They're doing great!")

answer = input("Enter your answer: ").lower()
answer_history.append(answer)

if answer == "a":
	scores[0] +=3 
elif answer == "b":
	scores[1] +=3
elif answer == "c":
	scores[2] +=1
elif answer == "d":
	scores[3] +=2
elif answer == "e":
	scores[4] +=-3
	
bigger_index = 0

if scores[0] > scores[1]: 
	bigger_index = 0 
else: 
	bigger_index = 1
if scores[bigger_index] < scores[2]:
	bigger_index = 2  
if scores[bigger_index] < scores[3]:
	bigger_index = 3 
if scores[bigger_index] < scores[4]:
	bigger_index = 4
	
print("You've entered:", answer_history)

if bigger_index <= 0:
	print("Your opinion stinks")
else:
	print("You know ball")
