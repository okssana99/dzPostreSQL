#покращений код з додаванням усіх вимог:
import datetime

class Employee:
    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def work(self):
        return "I come to the office."

    def check_salary(self):
        today = datetime.date.today()
        first_day_of_month = today.replace(day=1)
        work_days = self._count_work_days(first_day_of_month, today)
        return work_days * self.daily_salary

    def _count_work_days(self, start_date, end_date):
        work_days = 0
        current_date = start_date
        while current_date <= end_date:
            if current_date.weekday() < 5:  
                work_days += 1
            current_date += datetime.timedelta(days=1)
        return work_days

    def __str__(self):
        return f"Employee: {self.name}"

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


class Developer(Employee):
    def __init__(self, name, daily_salary, tech_stack):
        super().__init__(name, daily_salary)
        self.tech_stack = tech_stack

    def work(self):
        return "I come to the office and start to coding."

    def __str__(self):
        return f"Developer: {self.name}"

    def __eq__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) == len(other.tech_stack)
        return False

    def __add__(self, other):
        name = self.name + ' ' + other.name
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        salary = max(self.daily_salary, other.daily_salary)
        return Developer(name, salary, tech_stack)


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        return f"Recruiter: {self.name}"



