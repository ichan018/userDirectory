userList = []

def CheckLogin(userName,pwd):
    for x in range(len(userList)):
        if(userName == userList[x].userName):
           if(pwd == userList[x].pwd):
                return 2 #correct name, correct pwd
           return 1 # correct name and incorrect password
    return 0 # incorrect name and incorrect password

