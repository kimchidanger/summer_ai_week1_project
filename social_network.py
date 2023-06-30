#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_classes
import social_network_ui

p1 = Person("Eli", "15")
p2 = Person("John", "14")
p3 = Person("Jack", "17")  


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
            username = input("What is your name?")
            userage = input("What is your age?")


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
                    if inner_menu_choice1 == "2":
                        print("")
                        print("Your Current Name is:", username)
                        username = input("Changed Name?")
                    if inner_menu_choice1 == "3":
                        break

                if inner_menu_choice == "2":
                    for person in ai_social_network.list_of_people:
                        print(person.id)

                

                if inner_menu_choice == "5":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
