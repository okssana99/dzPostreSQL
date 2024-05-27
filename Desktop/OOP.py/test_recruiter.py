import unittest
from recruiter import Recruiter #type: ignore


class TestRecruiter(unittest.TestCase):
    def setUp(self):
        print("\nRunning setUp method...")
        self.recruiter_1 = Recruiter("John Doe", 150, ["Python", "Java"], "john.doe@example.com")
        self.recruiter_2 = Recruiter("Jane Doe", 180, ["JavaScript", "HTML"], "jane.doe@example.com")

    def tearDown(self):
        print("Running tearDown method...")

    def test_work(self):
        print("Running test_work...")
        self.assertEqual(self.recruiter_1.work(), "I come to the office and start to search for candidates.")
        self.assertEqual(self.recruiter_2.work(), "I come to the office and start to search for candidates.")

    def test_eq(self):
        print("Running test_eq...")
        self.assertTrue(self.recruiter_1 == self.recruiter_1)
        self.assertFalse(self.recruiter_1 == self.recruiter_2)

    def test_add(self):
        print("Running test_add...")
        recruiter_3 = self.recruiter_1 + self.recruiter_2
        self.assertEqual(recruiter_3.name, "John Doe Jane Doe")
        self.assertEqual(len(recruiter_3.tech_stack), 3)
        self.assertTrue(150 <= recruiter_3.daily_salary <= 180)

if __name__ == '__main__':
    unittest.main()