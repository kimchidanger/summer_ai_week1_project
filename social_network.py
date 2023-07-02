#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_classes
import social_network_ui

username1 = "Eli"
usernick1 = "LOL"
userage1 = "15"
username2 = "John"
usernick2 = "WOW"
userage2 = "14"
username3 = "Jack"
usernick3 = "JackAttack"
userage3 = "17"
mode = 4
current_mode = 4

p1 = Person(username1, usernick1, userage1)
p2 = Person(username2, usernick2, userage2)
p3 = Person(username3, usernick3, userage3)

#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()
            usernick = input("What do you want your username to be?")
            usernick4 = usernick
            username = input("What is your name?")
            username4 = username
            userage = input("What is your age?")
            userage4 = userage
            current_user = usernick4
            p4 = Person(username4, usernick4, userage4)

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "1":
                    print("")
                    print("1. Change Username")
                    print("2. Change Name")
                    print("3. Quit")
                    inner_menu_choice1 = input("Please Choose a number: ")
                    if inner_menu_choice1 == "1":
                        print("")
                        print("Your Current Username is:", usernick)
                        usernick = input("Changed Username?")
                        if mode == 1:
                            usernick1 = usernick
                        if mode == 2:
                            usernick2 = usernick
                        if mode == 3:
                            usernick3 = usernick
                        if mode == 4:
                            usernick4 = usernick
                    if inner_menu_choice1 == "2":
                        print("")
                        print("Your Current Name is:", username)
                        username = input("Changed Name?")
                        if mode == 1:
                            username1 = username
                        if mode == 2:
                            username2 = username
                        if mode == 3:
                            username3 = username
                        if mode == 4:
                            username4 = username
                    if inner_menu_choice1 == "3":
                        break

                if inner_menu_choice == "2":
                    print("")
                    for person in ai_social_network.list_of_people:
                        print(person.id)
                    friend = input("Pick a user to friend: ")
                    if friend == "Eli":
                        if p1 in person.friendlist:
                            print("Eli is already your friend")
                        else:
                            person.friendlist.append(p1)
                    if friend == "John":
                        if p2 in person.friendlist:
                            print("John is already your friend")
                        else:
                            person.friendlist.append(p2)
                    if friend == "Jack":
                        if p3 in person.friendlist:
                            print("Jack is already your friend")
                        else:
                            person.friendlist.append(p3)
                
                if inner_menu_choice == "3":
                    print("")
                    for person in person.friendlist:
                        print(person.id)
                    print("")
                    print("1. Remove Friend")
                    print("2. Block Friend")
                    print("3. Quit")
                    inner_menu_choice2 = input("Please Choose a number: ")
                    if inner_menu_choice2 == "1":
                        for person in person.friendlist:
                            print(person.id)
                        friend_remove = input("Remove Which Friend? ")
                        if friend_remove == person.friendlist:
                            person.friendlist.pop
                    if inner_menu_choice2 == "2":
                        for person in person.friendlist:
                            print(person.id)
                        friend_block = input("Block Which Friend? ")
                        if friend_block in person.friendlist:
                            if friend_block == username1:
                                while current_mode == mode
                                    ai_social_network.list_of_people.pop
                                    person.friendlist.pop
                
                if inner_menu_choice == "4":
                    print("")
                    print("1. Send message")
                    print("2. View message")
                    inner_menu_choice3 = input("Please Choose a number: ")
                    if inner_menu_choice3 == "1":
                        for person in person.friendlist:
                            print(person.id)
                        messagedirect = input("Send message to which person? ")
                        if messagedirect == "Eli":
                            message12 = []
                            message12.append(input("What would you like to send? "))       
                            print(current_user, ": ", message12)             
                        
                if inner_menu_choice == "5":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

                if inner_menu_choice == "6":
                    print("")
                    if mode == 1:
                        print("Name: " + username2 + ", Username: " + usernick2)
                        print("Name: " + username3 + ", Username: " + usernick3)
                        print("Name: " + username4 + ", Username: " + usernick4)
                    if mode == 2:
                        print("Name: " + username1 + ", Username: " + usernick1)
                        print("Name: " + username3 + ", Username: " + usernick3)
                        print("Name: " + username4 + ", Username: " + usernick4)
                    if mode == 3:
                        print("Name: " + username1 + ", Username: " + usernick1)
                        print("Name: " + username2 + ", Username: " + usernick2)
                        print("Name: " + username4 + ", Username: " + usernick4)
                    if mode == 4:
                        print("Name: " + username1 + ", Username: " + usernick1)
                        print("Name: " + username2 + ", Username: " + usernick2)
                        print("Name: " + username3 + ", Username: " + usernick3)

                    current_user = input("Pick user (enter name): ")
                    if current_user == username1:
                        username = username1
                        usernick = usernick1
                        userage = userage1
                        mode = 1
                        current_mode = 1
                    if current_user == username2:
                        username = username2
                        usernick = usernick2
                        userage = userage2
                        mode = 2
                        current_mode = 2
                    if current_user == username3:
                        username = username3
                        usernick = usernick3
                        userage = userage3
                        mode = 3
                        current_mode = 3
                    if current_user == username4:
                        username = username4
                        usernick = usernick4
                        userage = userage4
                        mode = 4
                        current_mode = 4

        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()