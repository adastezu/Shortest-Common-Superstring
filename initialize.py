from classes import *
def initleftavailable(leftavailable):
	i=0
	n=len(leftavailable)
	while i<n:
		leftavailable[i]=1
		i=i+1

def initrightavailable(rightavailable):
	i=0
	n=len(rightavailable)
	while i<n:
		rightavailable[i]=1
		i=i+1

def initleftend(leftend):
	i=0
	n=len(leftend)
	while i<n:
		leftend[i]=i
		i=i+1

def initrightend(rightend):
	i=0
	n=len(rightend)
	while i<n:
		rightend[i]=i
		i=i+1

def initedges(a):
	edges=[]
	n=len(a)
	for i in range(n):
		for j in range(n):
			if not (i==j):
				edges.append(edge(a[i][j],(i,j)))
	return edges

def initsuccessor(successor):
	i=0
	n=len(successor)
	while i<n:
		successor[i]= i
		i=i+1

def initpredecessor(predecessor):
	i=0
	n=len(predecessor)
	while i<n:
		predecessor[i]= i
		i=i+1

