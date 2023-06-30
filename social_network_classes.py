# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
            # you can save objects of people on the network in this list
        p1 = Person("Eli", "15")
        p2 = Person("John", "14")
        p3 = Person("Jack", "17")  

        self.list_of_people.append(p1)
        self.list_of_people.append(p2)
        self.list_of_people.append(p3)


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
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.indox = []
        
    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        pass

    def send_message(self, friend_name, message):
        #implement sending message to friend here
        pass
