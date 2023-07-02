# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
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

        p1 = Person(username1, usernick1, userage1)
        p2 = Person(username2, usernick2, userage2)
        p3 = Person(username3, usernick3, userage3)

        self.list_of_people.append(p1)
        self.list_of_people.append(p2)
        self.list_of_people.append(p3)
# you can save objects of people on the network in this list

    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here
        print("Creating ...")
        pass


class Person:
    def __init__(self, name, user, age):
        self.id = name
        self.username = user
        self.year = age
        self.friendlist = []
        self.indox = []
        
    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        pass

    def send_message(self, friend_name, message):
        #implement sending message to friend here
        pass
