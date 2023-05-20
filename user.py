class User:
    def __init__(self,userName,pwd):
        self.userName = userName;
        self.pwd = pwd
        self.msg = ""
  
    def ViewMessage(self):
        print("Your message is: ",self.msg)

    def EditMessage(self):
        print("Your current message is: ",self.msg)
        newMessage = input("Write your new message here: ")
        self.msg = newMessage
        print("Your new message is: ",self.msg)
   
        
