import itertools
from graph_form import *
#def maximum(S,k,v,dictionary):
#	m=0
#	for i in S:
#		#print(i)
#		#print(S)
#		#print(dictionary[(i,S)])
#		if not (i==v):
##			print("inside maximum {0},{1},{2}".format(i,v,S))
#			m1=max(m,weight(k,i)+dictionary[((i,v),S)][0])
#			if(m1>=m):
#				mv=i
#				m=m1
#				
#	return (m,mv)

def maximum(e,v,P,OPT):
	m=0
	for f in P:
		if not(f==v):
			m1=weight(e,f) + OPT[(f,v),frozenset(P)][0]
			if(m1>=m):
				m=m1
				mv=f
	return (m,mv)

def findsubsets(S,m):
	return set(itertools.combinations(S, m))

#def dp(S,u,v):
#	dictionary={}
#	n=len(S)
#	
#	for e in S:
#		if not(e==v):
#			dictionary[((e,v),frozenset({e,v}))]=(weight(e,v),v)
#	i=3
#	while i<(n+1):
#		A=findsubsets(S,i) #findsubsets(S,i) returns a set of subsets of S on cardinality i
#		for j in S:
#			for k in A:
#				if j in k and  not(j==v) and v in k:
#					k1=set(k)
#					d=dictionary
##					print("{0},{1},{2}".format(k1,j,v))
#					dictionary[((j,v),frozenset(k1))]= maximum(frozenset((k1-{j})),j,v,d)#OPT_j[k]=max_{v\in k\{j} }[ov(j,v)+OPT_v[k\j]]
#					#the maximum function calculates that max.The arguments in the function are those used in the term.
#					
#		i=i+1
#	return dictionary
#	
def dp(S,u,v):
	OPT={}
	n=len(S)
	for e in S :
		if not(e==v):
			OPT[(e,v),frozenset({e,v})]=(weight(e,v),v)
	i=3
	while i<(n+1):
		A=findsubsets(S,i)
		for P in A:
			if v in P:
				for e in P:
					if not (e==v):
						d=OPT
						OPT[(e,v),frozenset(P)]=maximum(e,v,set(P)-{e},d)
		i=i+1
#	print OPT
	return OPT

def OPT(S,u,v):
	x=set(S)
	lst=[u]
	table=dp(S,u,v)
	v1=u
	while (len(x)>1):
	#	print(len(x))
	#	print("{0},{1},{2}".format(v1,v,x))
	#	print(table[(v1,v),frozenset(x)])
		v2=table[(v1,v),frozenset(x)][1]
		x.remove(v1)
#		print(v2)
		lst.append(v2)
		v1=v2
	return lst
#	t=len(S)
#	u=S[0]
#	v=S[t-1]
#	x=set(S)-{u}-{v}
#	x=frozenset(x)
#	table=dp(S,u,v)
#	m=0
## OPT[V]=max_{v\in V}OPT[_v(V)]
#	for w in x:
#		m1=max(table[((w,v),x)][0],m)
#		if (m1>m):
#			mv=v
#			m=m1
#	if(m==0):
#		return(m,set(S).pop())
#	else:
#		return (m,mv)


#def OPTp(S,u,v):
#	x=set(S)
#	table=dp(S,u,v)
#	t=table[(u,v),frozenset(x)][0]
#	lst=[]
#	if(v[0]==0):
#		return S
#	else:
#		p=v[1]
#		#lst.append(v[1])
#		while not (len(x)==0):
#			p1=p
#			p=(table[(p,frozenset(x))])[1]
#			lst.append(p1)
#			x=x-{p1}
#		return lst

