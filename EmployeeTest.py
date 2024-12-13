from ast import increment_lineno
import unittest
from EmployeeCreator import Employee

class EmployeeTest(unittest.TestCase):
    
    def setUp(self):
        self.employee=Employee("Olayiwola","Ladipo",500000)
    
    def test_give_default_raise(self):
        self.employee.giveRaise()
        increment=self.employee.salary
        self.assertEqual(increment,505000)

    def test_give_custom_raise(self):
        self.employee.giveRaise(200)
        increment=self.employee.salary
        self.assertEqual(increment,500200)

if __name__=="__main__":
    unittest.main()