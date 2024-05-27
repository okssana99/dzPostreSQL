import unittest
from employee import Employee #type: ignore


class TestEmployee(unittest.TestCase):
    def test_email_saving(self):
        employee = Employee("John Doe", 100, "john.doe@example.com")
        self.assertTrue(employee.save_email())

    def test_email_validation(self):
        employee = Employee("Jane Doe", 120, "jane.doe@example")
        self.assertFalse(employee.validate_email(employee.email))

    def test_check_salary(self):
        employee = Employee("John Doe", 100, "john.doe@example.com")
        self.assertEqual(employee.check_salary(), 2000)

if __name__ == '__main__':
    unittest.main()