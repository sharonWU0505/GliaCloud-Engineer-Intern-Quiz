import sys

global number 
global factor1
global factor2
global factor3
number = 1000
factor1 = 3
factor2 = 5
factor3 = 15

def isMultiple(a, b):
	if a % b == 0:
		return 1
	else:
		return 0

def main():
	result = 0
	for i in range(3, number):
		if isMultiple(i, factor1) == 1:
			result += i
		else:
			if isMultiple(i, factor2) == 1 and isMultiple(i, factor3) == 0:
				result += i
	#print the answer
	print(result)
	return result


if __name__=="__main__":
	main()