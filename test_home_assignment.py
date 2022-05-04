import unittest
from .home_assignment import Placeholder

class TestPlaceholder(unittest.TestCase):
    def setUp(self):
        self.place_holder=Placeholder()

    def test_decision_tre_node(self):
        # do something with self.place_holder
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()