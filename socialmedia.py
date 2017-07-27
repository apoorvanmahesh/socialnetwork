#user_input = input("What is your username?")
usernameArray=[]
addName = True
class User():

    def __init__(self,name):
        self.connections=[]
        self.name = name

    def addConnection(self,invite):
        self.connections.append(invite)
        print("Your connections: %s." % self.connections)

A = User("Vee")
B = User("Maddie")
C = User("Nisha")
D= User("Apoorva")
usernameArray.append(A)
usernameArray.append(B)
usernameArray.append(C)
usernameArray.append(D)



while True:
    addName = True
    user_input = input("What username do you want?")
    x = User(user_input)

    #print(usernameArray[0].name)
    for i in range (len(usernameArray)):
        if user_input == usernameArray[i].name:
            addName = False
            print("Sorry, your username has already been taken. Please choose another one.")
            break
    if addName == True:
        usernameArray.append(x)

    print(" ")
    print(" ")

    for i in range (len(usernameArray)):
        print(usernameArray[i].name)
    print("Thanks for making an account with us! You can now conenct with other people!")

    yourName = input("What is your username?")
    index = None
    userFound = False
    for i in range (len(usernameArray)):
        if yourName == usernameArray[i].name:
            index = i;
            userFound = True
            break
    if userFound == False:
        print("Sorry, that username does not exist.")
    else:
        inviteName = input("Who do you want to connect with?")
        usernameArray[index].addConnection(inviteName)
