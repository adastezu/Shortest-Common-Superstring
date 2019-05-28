def verifysuperstring(S,x):
	n=len(S)
	flag=1
	for i in range(n):
		if not(S[i] in x):
			return False
	return True


