# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. Send and view all my messages")
    print("5. <- Go back ")
    return input("Please Choose a number: ")

def myfunc(self):
    print("Hi, my name is " + self.id + "," + self.year + "years old")


