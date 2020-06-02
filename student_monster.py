from monster import Monster


class Student(Monster):

    def __init__(self, name, tax, fur, student_no, skill_list):
        self.student_NO = student_no
        self.skills = skill_list
        super().__init__(name, tax, fur)

    # This method takes a string argument and adds it to the list of skills for student monsters.
    def add_skills(self, new_skill):
        self.skills.append(new_skill)

    # This method displays an object's attributes in a formatted manner using a dictionary.
    def get_student(self):
        attributes = {
            "Name          ": self.name,
            "Tax number    ": self.tax,
            "Fur colour    ": self.get_fur(),
            "Student number": self.student_NO,
            "Skills        ": self.skills
        }
        for i in attributes:
            print(i, " : ", attributes[i])
        return ""

    # Asks user for input and then creates object based on the inputs
    def set_student(self):
        add_name = input("Enter the name of your new student: ")
        add_tax = input("Enter their tax number")
        add_fur = input("Enter their fur colour ")
        add_stud_num = input("Enter their student number ")
        add_skills = input("Enter their skills ")

        self.__init__(self, add_name, add_tax, add_fur, add_stud_num, add_skills)
