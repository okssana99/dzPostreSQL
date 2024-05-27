import unittest
from candidate import Candidate # type: ignore

class TestCandidate(unittest.TestCase):
    def test_init(self):
        candidate = Candidate("John", "Doe", "john.doe@example.com", "Python;Django", "Python", 9)
        self.assertEqual(candidate.first_name, "John")
        self.assertEqual(candidate.last_name, "Doe")
        self.assertEqual(candidate.email, "john.doe@example.com")
        self.assertEqual(candidate.tech_stack, ["Python", "Django"])
        self.assertEqual(candidate.main_skill, "Python")
        self.assertEqual(candidate.main_skill_grade, 9)

    def test_full_name(self):
        candidate = Candidate("John", "Doe", "john.doe@example.com", "Python;Django", "Python", 9)
        self.assertEqual(candidate.full_name, "John Doe")

    def test_generate_candidates_from_csv_string(self):
        csv_string = """first_name,last_name,email,tech_stack,main_skill,main_skill_grade
John,Doe,john.doe@example.com,Python;Django,Python,9
Jane,Doe,jane.doe@example.com,JavaScript;React,JavaScript,8"""
        candidates = Candidate.generate_candidates(csv_string)
        self.assertEqual(len(candidates), 2)
        self.assertEqual(candidates[0].full_name, "John Doe")
        self.assertEqual(candidates[1].full_name, "Jane Doe")

    def test_generate_candidates_from_csv_file(self):
        candidates = Candidate.generate_candidates("tests/candidates.csv")
        self.assertEqual(len(candidates), 2)
        self.assertEqual(candidates[0].full_name, "John Doe")
        self.assertEqual(candidates[1].full_name, "Jane Doe")

if __name__ == '__main__':
    unittest.main()