# Python3 program to find a list of uncommon words

# Function to return all uncommon words
def UncommonWords(A, B):
	A=A.split()
	B=B.split()
	x=[]
	for i in A:
		if i not in B:
			x.append(i)
	for i in B:
		if i not in A:
			x.append(i)
	x=list(set(x))
	return x
			

# Driver Code
A = "Python Algorithms"
B = "Learning from Github and Hacktoberfests"

# Print required answer
print(UncommonWords(A, B))
