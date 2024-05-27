import unittest
from developer import Developer #type: ignore


class TestDeveloper(unittest.TestCase):
    def setUp(self):
        print("\nRunning setUp method...")
        self.developer_1 = Developer("John Doe", 100, ["Python", "Java"], "john.doe@example.com")
        self.developer_2 = Developer("Jane Doe", 120, ["JavaScript", "HTML"], "jane.doe@example.com")

    def tearDown(self):
        print("Running tearDown method...")

    def test_work(self):
        print("Running test_work...")
        self.assertEqual(self.developer_1.work(), "I come to the office and start to coding.")
        self.assertEqual(self.developer_2.work(), "I come to the office and start to coding.")

    def test_eq(self):
        print("Running test_eq...")
        self.assertTrue(self.developer_1 == self.developer_1)
        self.assertFalse(self.developer_1 == self.developer_2)

    def test_add(self):
        print("Running test_add...")
        developer_3 = self.developer_1 + self.developer_2
        self.assertEqual(developer_3.name, "John Doe Jane Doe")
        self.assertEqual(len(developer_3.tech_stack), 3)
        self.assertTrue(100 <= developer_3.daily_salary <= 120)

if __name__ == '__main__':
    unittest.main()