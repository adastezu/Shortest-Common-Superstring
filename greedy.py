from graph_form import *
from initialize import *
from reportstring import *
from classes import *

def sort(edges):
	i=0
	n=len(edges)
	sortededges =sorted(edges,key=lambda x: x.weight,reverse=True)
	while(i<n):
		u=sortededges[i]
#		u=edges[i]
#		print("{0},{1}".format(u.e,u.weight))
		i=i+1
	return sortededges
	
def updaterightend(e,predecessor,rightend):
	u=e[0]
	v=e[1]
	rightend[u]=rightend[v]
	while not(predecessor[u]==u):
		rightend[predecessor[u]]=rightend[v]
		u=predecessor[u]
	

def updateleftend(e,successor,leftend):
	u=e[0]
	v=e[1]
	leftend[v]=leftend[u]
	while not(successor[v]==v):
		leftend[successor[v]]=leftend[u]
		v=successor[v]
#		print v
	


#def find(a,u):
#	n=len(a)
#	m=len(a[0])
#	for p in range(n):
#		for q in range(m):
#			if(a[p][q]==u):
#				return (p,q)
#				


def trymerge(edgem,leftavailable,rightavailable,leftend,rightend):
	u=edgem.e[0]
	v=edgem.e[1]
	if (leftavailable[u]==1)and (rightavailable[v]==1) and not(leftend[u]==v):
		return True
	else:
		return False


def greedy(S):
	
	a=adj_matrix(S)
	n=len(S)
	leftavailable=[0 for p in range(n)]
	rightavailable=[0 for p in range(n)]
	leftend=[0 for p in range(n)]
	rightend=[0 for p in range(n)]
	successor=[0 for p in range(n)]
	predecessor=[0 for p in range(n)]
	initleftavailable(leftavailable)
	initrightavailable(rightavailable)
	initleftend(leftend)
	initrightend(rightend)
	initsuccessor(successor)
	initpredecessor(predecessor)
	edges=initedges(a)
	sortededges=sort(edges)
	for i in range(len(sortededges)):
		if trymerge(sortededges[i],leftavailable,rightavailable,leftend,rightend):
#			
#			print (sortededges[i].e)
			leftavailable[sortededges[i].e[0]]=0
#			print(leftavailable)
			rightavailable[sortededges[i].e[1]]=0
#			print(rightavailable)
#			leftend[sortededges[i].e[1]]=leftend[sortededges[i].e[0]]
#			print(leftend)
#			rightend[sortededges[i].e[0]]=rightend[sortededges[i].e[1]]
#			print(rightend)
			successor[sortededges[i].e[0]]=sortededges[i].e[1]
#			print(successor)
			predecessor[sortededges[i].e[1]]=sortededges[i].e[0]
#			print(predecessor)
			updaterightend(sortededges[i].e,predecessor,rightend)
			updateleftend(sortededges[i].e,successor,leftend)
			
	sequence = stringsequence(successor,leftend[0])
#	print(sequence)
	
	return report(sequence,S)
