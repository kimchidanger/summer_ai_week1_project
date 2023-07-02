# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [Person("Eli", "LOL", 15), Person("John", "WOW", 14), Person("Jack", "JackAttack", 17)] # this instance variable is initialized to an empty list when social network is created, 
        self.list_of_names = ["Eli", "John", "Jack"]
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
        self.inbox = []
        
    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        pass

    def send_message(self, friend_name, message):
        #implement sending message to friend here
        pass

    def change_name(self, name):
        self.id = name

    def change_username(self, username):
        self.username = username
