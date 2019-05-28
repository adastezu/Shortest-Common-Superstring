def preprocess(x):
	n=len(x)
	y=[]
	i=0
	while i<n:
		bit=True
		j=0
		while j<n :
			if (x[i] in x[j]) and not(i==j):
				i=i+1
				bit=False
				break
			j=j+1
		if bit==True:
			y.extend([x[i]])
			i=i+1
	return y


