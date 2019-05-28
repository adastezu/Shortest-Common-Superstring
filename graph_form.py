#calculating length of prefix
def weight(x,y):
	n1=len(x)
	n2=len(y)
	n=min(n1,n2)
	i=n
	while i>0 :
		if(x.endswith(y[0:i],0,n1)):
			break
		i=i-1
	return i

def adj_matrix(x):
	n=len(x)
	a=[[0 for p in range(n)] for q in range(n)] 
	i=0
	while(i<n):
		j=0
		while(j<n):
			if not(i==j):
				a[i][j]=weight(x[i],x[j])
			else:
				a[i][j]=0
			j=j+1
		i=i+1
	return a

