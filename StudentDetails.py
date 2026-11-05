class student_details:
    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

William = student_details("William", 8, 78)
Reuben = student_details("Reuben", 10, 93)

print("{} is in Grade {} ".format(William.name, William.grade))
print("{} is in Grade {}".format(Reuben.name, Reuben.grade))
print("William got {} percent.".format(William.percentage))
print("Reuben got {} percent.".format(Reuben.percentage))
