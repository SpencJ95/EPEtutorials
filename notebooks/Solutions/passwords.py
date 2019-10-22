OUTFILE = "../OtherFiles/passwordSolution.txt"

def addUser(username,password,score):
	# check that username and password aren't empty
	if username == '' or password == '':
		raise ValueError("Username and password must be at least 1 character long.")

	f = open(OUTFILE,"a+")
	f.write("%s %s %d\n" % (username, password, score))
	f.close()

def getScore(username,password):
	f = open(OUTFILE,"r")
	# loops through each line l
	for l in f.readlines():
		userData = l.split()
		if userData[0] == username and userData[1] == password:
			f.close()
			return userData[2]
	f.close()
	# couldn't find username or password :(
	raise ValueError("User does not exist or password does not match.")

	# ALTERNATIVE SOLUTION
	# turn file into string and use .find() method
	# strFile = f.read()
	# a = lines.find(username+" "+password)
	# if a > -1:
	# 	return lines[a:].split()[2]
	

def removeUser(username,password):
	f = open(OUTFILE,"w")
	lines = f.readlines()
	# loops through each line, where
	for i in range(0,len(lines)):
		userData = lines[i].split()
		if userData[0] == username and userData[1] == password:
			f.write(" ".join(lines[:i]+lines[i+1:]))
			f.close()
			return userData
	f.close()
	raise ValueError("User does not exist or password does not match.")

def eraseFile():
	f = open(OUTFILE,"w").close()

if __name__ == "__main__":
	addUser("alice","abc",100)
	print(getScore("alice","abc"))

	addUser("bob","wasd",1337)
	print(getScore("bob","wasd"))
