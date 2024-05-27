class Employee:
    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def work(self):
        return "I come to the office."


    def __str__(self):
        return f"Employee: {self.name}"


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."


    def __str__(self):
        return f"Recruiter: {self.name}"


class Developer(Employee):
    def work(self):
        return "I come to the office and start to coding."


    def __str__(self):
        return f"Developer: {self.name}"


    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.daily_salary == other.daily_salary
        return False

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.daily_salary < other.daily_salary
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.daily_salary > other.daily_salary
        return NotImplemented


employee1 = Employee("John", 100)
recruiter1 = Recruiter("Alice", 120)
developer1 = Developer("Bob", 150)


print(employee1.work())  
print(recruiter1.work())  
print(developer1.work())  


print(employee1)  
print(recruiter1)  
print(developer1)  


print(developer1 == recruiter1)  
print(developer1 > recruiter1)   
print(developer1 < recruiter1)   
