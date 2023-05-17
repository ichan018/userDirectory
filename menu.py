userList = []

def UserLogin(loc):
   print("Do login menu")

#should return string, handle username and password 
def CheckLogin():
    # create while loop involving username and password
    ifContinue = 1
    ifLoginWorked = 0
    while(ifContinue):
       inputUser = input("Enter username:")
       #inputPwd = input("Enter password:")
       curr = 0
       while curr < len(userList) and not(ifLoginWorked):
          if(inputUser == userList[curr].userName):
             #userName correct, make sure password is correct
             inputPwd = input("Enter password:")
             if(inputPwd == userList[curr].pwd):
                 ifContinue = 0
                 ifLoginWorked = 1
                 print("Login successful")
                 #UserLogin(x)
             else:
                 print("Password incorrect, try again")
          curr += 1 #increment

    if(ifLoginWorked):
       UserLogin(curr)
    else:
       SaveData()


def SaveData():
   #json_file = open('userList.json','w')
   #json_file.write(json.dumps(userList))
   #json_file.close()
   print("Thank you for enjoying this program")
   print("Data will be able to be saved soon")


