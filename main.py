from user import *
from menu import *

ifContinue = 1

def UserLogin():
     inputUser = input("Enter username:")
     inputPwd = input("Enter password:")

     loginInfo = CheckLogin(inputUser,inputPwd)

     if loginInfo == 2:
         print("Success!")

def AddUser(name,pwd):
     userList.append(User(name,pwd))


while(ifContinue == 1):
    loginVal = -1
    highestChoice = 3
    while(loginVal < 0 or loginVal > highestChoice ):
        print("Welcome to Ivan's Server. What would you like to do?")
        print("0: Exit")
        print("1: Login")
        print("2: Add User")
        print("3: DEBUG: Figure out all Users")
        loginVal = int(input(""))

    if(loginVal == 0):
        ifContinue = 0
        break
    elif(loginVal == 1):
        UserLogin()
    elif(loginVal == 2):
        newUserName = input("Add username (no spaces, please)")
        newPwd = input("Add password:")
        AddUser(newUserName,newPwd)
    elif(loginVal == 3):
        for x in range(len(userList)):
            print(userList[x].userName, userList[x].pwd)
