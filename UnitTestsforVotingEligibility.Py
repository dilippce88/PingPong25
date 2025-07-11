class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def can_vote(self):
        return self.age >= 18

------------------------------------------------------------------------------

import unittest
from user import User

class TestUserVoting(unittest.TestCase):

    def test_user_can_vote(self):
        user = User("Alice", 25)
        self.assertTrue(user.can_vote(), "User aged 25 should be able to vote.")

    def test_user_cannot_vote(self):
        user = User("Bob", 17)
        self.assertFalse(user.can_vote(), "User aged 17 should NOT be able to vote.")

    def test_user_exactly_18_can_vote(self):
        user = User("Charlie", 18)
        self.assertTrue(user.can_vote(), "User aged 18 should be able to vote.")

    def test_user_with_negative_age(self):
        user = User("Dave", -5)
        self.assertFalse(user.can_vote(), "User with negative age should NOT be able to vote.")

if __name__ == '__main__':
    unittest.main()