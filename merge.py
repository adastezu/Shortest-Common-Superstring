from graph_form import*
def overlap(x,y):
	n1=len(x)
	n2=len(y)
	n=min(n1,n2)
	i=n
	while i>0 :
		if(x.endswith(y[0:i],0,n1)):
			break
		i=i-1
	return y[0:i]

def merge(x,y):
	i=weight(x,y)
	n=len(y)
	return (x+y[i:n])

def superstring(S):
	n=len(S)
	S1=list(S)
	if n>1:
		u=S[0]
		S.remove(S[0])
		return merge(u,superstring(S))
	else:
		return S[0]

def callsuperstring(S):
	S1=list(S)
	return superstring(S1)
