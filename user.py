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

    @classmethod
    def find_user(cls, username):
        '''
        find username using search terms
        '''
        for user in cls.userlist:
            if user.username == username:
                return  user

class Credentials:
    '''
    class that creates instaces of user accounts
    '''
    credentialslist = []

    def __init__(self, account ,username, email , passlock):
    
        self.account = account
        self.username=username
        self.email = email
        self.passlock = passlock

    def save_credentials(self):
        '''
        Method to save a users Credentials
        '''
        Credentials.credentialslist.append(self)

    def delete_credentials(self):
        '''
        delete credentials 
        '''
        Credentials.credentialslist.remove(self)  
       

        
