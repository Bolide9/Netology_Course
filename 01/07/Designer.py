from Employee import Employee


class Designer(Employee):
    def __init__(self, name, experience, prize=2):
        super().__init__(name, experience),
        self.prize = prize

    def check_for_upgrade(self):
        self.seniority += 1

        if self.seniority % 7 == 0:
            self.grade_up()

        return self.publish_grade()
