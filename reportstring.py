def stringsequence(successor,leftend):
	i=0
	j=leftend
	n=len(successor)
	sequence=[0 for p in range(n)]
	while not(successor[j]==j):
		sequence[i]=j
		j=successor[j]
		i=i+1
#		print(j)
	sequence[i]=j
#	print(i)
	return sequence

def report(sequence,S):
	i=0
	n=len(sequence)
	orderedstrings=[]
	while i<n:
		orderedstrings.append(S[sequence[i]])
		i=i+1
	return orderedstrings
