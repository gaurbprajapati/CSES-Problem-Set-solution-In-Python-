# This function generates all n
# bit Gray codes and prints the
# generated codes
def generateGray(n):
	
	# Base case
	if (n <= 0):
		return ["0"]
	if (n == 1):
		return [ "0", "1" ]
 
	# Recursive case
	recAns = generateGray(n - 1)
 
	mainAns = []
	
	# Append 0 to the first half
	for i in range(len(recAns)):
		s = recAns[i]
		mainAns.append("0" + s)
 
	# Append 1 to the second half
	for i in range(len(recAns) - 1, -1, -1):
		s = recAns[i]
		mainAns.append("1" + s)
 
	return mainAns
 
# Function to generate the
# Gray code of N bits
def generateGrayarr(n):
	
	arr = generateGray(n)
 
	# Print contents of arr
	print(*arr, sep = "\n")
 
# Driver Code
n=int(input())
generateGrayarr(n)
 