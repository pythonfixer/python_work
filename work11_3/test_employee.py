import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.my_employee = Employee('jack', 'ma', 30000)      
    
    def test_give_default_raise(self):
        self.my_employee.give_raise()        
        self.assertEqual(35000, self.my_employee.money)
    
    def test_give_custom_raise(self):
        self.my_employee.give_raise(8000)        
        self.assertEqual(38000, self.my_employee.money)
        
unittest.main()
