import random
import string

class User:
    """
    Create User class that generates new instances of a user.
    """
    userlist = []

    def __init__(self,firstname,lastname, username, password):
        """
       _init_ method that defines the properties of the object self.
        """
        self.firstname=firstname
        self.lastname=lastname
        self.username = username
        self.password = password

    def save_user(self):
            """
            A method that saves a new user instace into the user list
            """
            User.userlist.append(self)

    def delete_user(self):
        '''
        delete a user account
        '''
        User.userlist.remove(self)

        
