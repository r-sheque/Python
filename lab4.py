target = [6, 7, 8, 9, 10, 67]

max = target[0]
min = target[0]
sum = 0

for value in target:
	if value > max: 
		max = value	
	if value < min:
		min = value 
	sum += value  

print(f"The max is {max} , and the min is {min}")

len(target)
mean = sum / len(target)
print(mean)
	
