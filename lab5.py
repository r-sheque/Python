def fizzbuzz(num):
	if num < 0:
		return -1
			
	for i in range(num + 1):
		if i % 3 == 0 and i % 5 == 0:
			print("fizzbuzz")
			last_fizz_or_buzz = i 
		
		elif i % 3 == 0: 
			print("fizz")
			last_fizz_or_buzz = i
			
		elif i % 5 == 0: 
			print("buzz")
			last_fizz_or_buzz = i 
			
		else:
			print(i)
			
	return last_fizz_or_buzz
		
print(fizzbuzz(10))
print(fizzbuzz(31))
print(fizzbuzz(-2))
