import csv
import requests # type: ignore

class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Candidate: {self.full_name}"

    @classmethod
    def generate_candidates(cls, source):
        candidates = []
        if source.startswith("http"):
            response = requests.get(source)
            lines = response.text.split('\n')
        else:
            with open(source, 'r') as file:
                lines = file.readlines()
        csv_reader = csv.reader(lines)
        next(csv_reader)  
        for row in csv_reader:
            first_name, last_name, email, tech_stack, main_skill, main_skill_grade = row
            candidate = cls(first_name, last_name, email, tech_stack.split(';'), main_skill, int(main_skill_grade))
            candidates.append(candidate)
        return candidates

