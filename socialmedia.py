#user_input = input("What is your username?")
usernameArray=[]
addName = True
class User():
    def __init__(self,name):
        self.name = name
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
    user_input = input("What is your username?")
    x = User(user_input)
    #print(usernameArray[0].name)
    for i in range (len(usernameArray)):
        print(usernameArray[i].name)
        if user_input == usernameArray[i].name:
            addName = False
            print("Sorry, your username has already been taken. Please choose another one.")
            break
    if addName == True:
        usernameArray.append(x)

        #print(usernameArray[i].name)

    # if user_input not in username:
    #     username.append(x)
    # elif user_input in username:
    #     print("Sorry, your username has already been taken. Please choose another one.")
    # print(username)
    # print(username[0].name)
