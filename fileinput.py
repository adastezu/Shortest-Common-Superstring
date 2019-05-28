def readfile(filename):
	fr=open(filename,"r")
	fw=open("i.txt","w")
#	for i in range(100):
	s=fr.readlines()
#		if not(i%2==0):
#			print(s)
#			fw.write(s)
	n=len(s)
	s1=[]
	for i in range(n):
		if  not (i%2==0):
			n1=len(s[i])
			s1.append(s[i][0:n1-2])
	return s1


