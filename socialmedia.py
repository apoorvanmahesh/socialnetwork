#user_input = input("What is your username?")
username=[]

class User():
    def __init__(self,name):
        self.name = name



while True:
    #add usernames
    user_input = input("What is your username?")
    x = User(user_input)
    print(x.name)
    username.append(x)
    #Invitations...reference list of usernames and add them in order to messages
    
    # if user_input not in username:
    #     username.append(x)
    # elif user_input in username:
    #     print("Sorry, your username has already been taken. Please choose another one.")
    # print(username)
    # print(username[0].name)
