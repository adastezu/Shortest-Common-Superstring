from dp import*
def exactsequence(S):
	n=len(S)
	u=S[0]
	v=S[n-1]
	return OPT(S,u,v)
#	return S

def boost(S,m):
	n=len(S)
#	print(n)
	q=n/m
	r=n%m
	ns=[]
	i=1
	while i<(q+1):
		print("{0},{1}".format(((i-1)*m),(i*m)))
#		print(S[(i-1)*m:i*m])
		t=S[(i-1)*m:i*m]
		s=exactsequence(t)
		ns=ns+s
		i=i+1
	if not(r==0):
		t=S[q*m:n]
		ns=ns+exactsequence(t)
#	print(ns)
	return ns
