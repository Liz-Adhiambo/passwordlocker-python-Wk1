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

    def test_init(self):
            """
         test_init  Test case to chek if the object has been initialized correctly
            """
            self.assertEqual(self.new_user.username,'liz')
            self.assertEqual(self.new_user.password,'1234.')


if __name__ == "__main__":
    unittest.main()
