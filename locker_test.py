import unittest
from user import User
from user import Credentials

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('Elizabeth','Adhiambo','liz','1234.')

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.userlist = []

    def test_init(self):
            """
         test_init  Test case to chek if the object has been initialized correctly
            """
            self.assertEqual(self.new_user.username,'liz')
            self.assertEqual(self.new_user.password,'1234.')

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.userlist),1)


    def test_delete_user(self):
        '''
        check whether one can delete a user account
        '''
        self.new_user.save_user()
        test_user = User('Elizabeth', 'Adhiambo','liz','1234.')
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.userlist), 1)

    
    def test_find_user(self):
        '''
        find a user using username
        '''
        self.new_user.save_user()
        test_user = User('Elizabeth', 'Adhiambo','liz','1234.')
        test_user.save_user()
        found_user = User.find_user("liz")
        self.assertEqual(found_user.username, self.new_user.username)

 #Credentials Class Tests

class TestCredentials(unittest.TestCase):

    def setUp(self):
            '''
            setup before a test is run
            '''
            self.new_credentials = Credentials('Instagram','liz','adhiambo@gmail.com','abcd')
    def tearDown(self):
            '''
            clear list before any test is run
            '''
            Credentials.credentialslist = []

    
    def test_init(self):
        '''
        check if instances initialize as expected
        '''
        self.assertEqual(self.new_credentials.account, "Instagram")
        self.assertEqual(self.new_credentials.username, "liz")
        self.assertEqual(self.new_credentials.email, "adhiambo@gmail.com")
        self.assertEqual(self.new_credentials.passlock, "abcd")

    def test_save_credentials(self):
        '''
        check if credentials can be saved
        '''  
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentialslist),1)

    def test_delete_credentials(self):
        '''
        test if you can delete credentials test
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter','liz','adhiambo@gmail.com','abcd')
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentialslist), 1)

    def test_search_for_credentials(self):
        '''
        Test case to test if credentials can be searched 
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter','liz','adhiambo@gmail.com','abcd')
        test_credentials.save_credentials()
        find_credentials= Credentials.find_account("Twitter")
        self.assertEqual(find_credentials.account, test_credentials.account)


    
       

        

if __name__ == "__main__":
    unittest.main()
