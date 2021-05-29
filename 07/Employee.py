class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        self.grade = 2

    def grade_up(self):
        self.grade += 1
        print('Уровень повышен!')

    def publish_grade(self):
        print(self.name, self.grade)
