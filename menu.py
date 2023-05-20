import pickle
import os.path

userList = []

def UserLogin(loc):
   print("Do login menu")
   ifContinue = 1

   while(ifContinue):
      print("What would you like to do?")
      print("0: Logout")
      print("1: View Saved Message")
      print("2: Edit Saved Message")
      userChoice = int(input(""))

      if(userChoice == 0):
         ifContinue = 0
      elif(userChoice == 1):
         userList[loc].ViewMessage()
      elif(userChoice == 2):
         userList[loc].EditMessage()

#should return string, handle username and password 
def CheckLogin():
    # create while loop involving username and password
    ifContinue = 1
    ifLoginWorked = 0
    while(ifContinue):
       inputUser = input("Enter username (press -1 to exit login prompts:")

       if(inputUser == "-1"):
           ifContinue = 0
           break

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
                 break
             else:
                 print("Password incorrect, try again")
          curr += 1 #increment

    if(ifLoginWorked):
       UserLogin(curr)

# if program previously run, list.txt should exist
def LoadData():
   print("Loading data ...")
   # load userList
   if os.path.exists("list.pkl"):
      #f = open("list.txt", "rb")
      #userList = pickle.load(f)
      #f.close()
      with open('list.pkl','rb') as input:
         userList = pickle.load(input)
   print("Data loaded")

def SaveData():
   #json_file = open('userList.json','w')
   #json_file.write(json.dumps(userList))
   #json_file.close()
   print("Thank you for enjoying this program")
   print("Data is saving")
   #f = open("list.txt","wb")
   #pickle.dump(userList,f)
   #f.close()
   with open('list.pkl','wb') as output:
      pickle.dump(userList,output)
   print("Data saved")


