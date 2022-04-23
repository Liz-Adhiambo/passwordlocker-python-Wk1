import unittest
from user import User

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


    

if __name__ == "__main__":
    unittest.main()
