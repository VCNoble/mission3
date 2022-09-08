__author__ = 'mission_3'

import unittest
from unit_test import Greeter

class mission(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter ()
        self.assertEqual(greeter.message, 'Hello World!')

    def test_default_greeting_set2(self):
        greeter2 = Greeter ()
        self.assertEqual(greeter2.message, 'hello%world')

    def test_default_greeting_set3(self):
        greeter3 = Greeter ()
        self.assertEqual(greeter3.message, '!hello world')
    
    def test_default_greeting_set4(self):
        greeter4 = Greeter ()
        self.assertEqual(greeter4.message, ';hello?world!')
    
    def test_default_greeting_set5(self):
        greeter5 = Greeter ()
        self.assertEqual(greeter5.message, 'hello;world')
    
    def test_default_greeting_set6(self):
        greeter6 = Greeter ()
        self.assertEqual(greeter6.message, 'Hello World?')
    
if __name__ == '__main__':
    unittest.main()