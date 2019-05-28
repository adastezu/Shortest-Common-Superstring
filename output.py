from input_s import input_strings
from preprocess import preprocess
import sys
from graph_form import *
from greedy import *
from merge import *
from boost import *
from fileinput import*
from verify import*
m=readfile("/home/avinandan/python experiments/MH0004.seq.fa")
#print(len(m))
i = input("Enter the number of strings to be processed from the file.\n")
x=m[1:i]
y=preprocess(x)
print "Running the greedy algorithm."
z= greedy(y)
u=callsuperstring(z)
print "Verifying the greedy superstring."
if verifysuperstring(x,u)== True:
	print "superstring verified."
else :
	sys.exit("There might be a bug in the greedy procedure.")
print "Length of the greedy superstring is ",len(u)
number_of_strings_for_boost = input("Enter the number of strings to boost the performance.\n")
t=boost(z,number_of_strings_for_boost)
#print(t)
print "Running the greedy algorithm with boosting procedure."
q=callsuperstring(t)
if verifysuperstring(x,q)== True:
	print "superstring verified."
else :
	sys.exit("There might be a bug in the boosting procedure.")
print "Length of the superstring after the boost is ",len(q)


#print(len(t))
