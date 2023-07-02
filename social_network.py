#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_classes
import social_network_ui

mode = 4
current_mode = 4

account_creation = False

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
            if account_creation == False:
                print("\nYou are now in the create account menu")
                ai_social_network.create_account()
                usernick = input("What do you want your username to be?")
                usernick4 = usernick
                username = input("What is your name?")
                username4 = username
                userage = input("What is your age?")
                userage4 = userage
                current_user = username4
                current_account = Person(username4, usernick4, userage4)
                ai_social_network.list_of_people.append(current_account)
                ai_social_network.list_of_names.append(username4)

                account_creation = True

        elif choice == "2":
            #Handle inner menu here
            inner_menu_choice = social_network_ui.manageAccountMenu()
            while True:
                if account_creation == True:
                    if inner_menu_choice == "1":
                        print("")
                        print("1. Change Username")
                        print("2. Change Name")
                        print("3. Quit")
                        inner_menu_choice1 = input("Please Choose a number: ")
                        if inner_menu_choice1 == "1":
                            print("")
                            print("Your Current Username is:", current_account.username)
                            usernick = input("Changed Username?")
                            current_account.change_username(usernick)
                        if inner_menu_choice1 == "2":
                            print("")
                            print("Your Current Name is:", current_account.id)
                            username = input("Changed Name?")
                            current_account.change_name(username)
                        if inner_menu_choice1 == "3":
                            break

                    if inner_menu_choice == "2":
                        print("")
                        for person in ai_social_network.list_of_names:
                            if person != current_user:
                                print(person)
                        friend = input("Pick a user to friend: ")
                        if friend in ai_social_network.list_of_names:
                            if friend in current_account.friendlist:
                                print(friend, " is already your friend")
                            else:
                                current_account.friendlist.append(friend)

                    if inner_menu_choice == "3":
                        print("")
                        for friend in current_account.friendlist:
                            print(friend)
                        print("")
                        print("1. Block Friend")
                        print("2. Quit")
                        inner_menu_choice2 = input("Please Choose a number: ")
                        if inner_menu_choice2 == "1":
                            print("")
                            friend_remove = input("Block Which Friend? ")
                            if friend_remove in current_account.friendlist:
                                print("works")
                                current_account.friendlist.remove(friend_remove)
                    
                    if inner_menu_choice == "4":
                        print("")
                        print("1. Send message")
                        print("2. View message")
                        inner_menu_choice3 = input("Please Choose a number: ")
                        if inner_menu_choice3 == "1":
                            for friend in current_account.friendlist:
                                print(friend)
                            messagedirect = input("Send message to which person? ")
                            if messagedirect in current_account.friendlist:
                                ai_social_network.list_of_people[ai_social_network.list_of_names.index(messagedirect)].inbox.append([input("What is your message? "), current_user])
                        if inner_menu_choice3 == "2":
                            for message in current_account.inbox:
                                print("'", message[0], "'", " from: ", message[1])  
                            
                    if inner_menu_choice == "5":
                        break
                    else:
                        inner_menu_choice = social_network_ui.manageAccountMenu()


                    if inner_menu_choice == "6":
                        print("")
                        for person in ai_social_network.list_of_names:
                            print(person)
                        switch = input("Pick user (enter name): ")
                        if switch in ai_social_network.list_of_names:
                            current_user = switch
                            current_account = ai_social_network.list_of_people[ai_social_network.list_of_names.index(switch)]
                else:
                    print("")
                    print("You need to make an account first")



        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break


        else:
            print("Your input is invalid. Try Again!")
       
        #restart menu
        choice = social_network_ui.mainMenu()

