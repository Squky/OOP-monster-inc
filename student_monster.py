from monster import Monster


class Student(Monster):

    def __init__(self,name,tax,fur,student_no,skill_list):
        self.student_NO = student_no
        self.skills = skill_list
        super().__init__(Monster,name,tax)
        super().set_fur(fur)        # the 'set_fur' method is needed because fur has been declared as private in the 'Monster' parent class

    def add_skills(self,new_skill): #This method takes a string argument and adds it to the list of skills for student monsters.
        self.skills.append(new_skill)


    def get_student(self):  # A simple way to display an objects attributes in a formatted manner

        attributes = {
            "name" : self.name,
            "tax" : self.tax,
            "fur colour" : self.get_fur(),
            "student number" : self.student_NO,
            "skills" : self.skills
        }
        for i in attributes:
            print (i, " : ", attributes[i])


        return ""

    def set_student(self):      # Asks user for input and then creates object based on the inputs
        add_name = input("Enter the name of your new student: ")
        add_tax = input("Enter their tax number")
        add_fur = input("Enter their fur colour ")
        add_stud_num= input("Enter their student number ")
        add_skills = input("Enter their skills ")

        self.__init__(self,add_name, add_tax, add_fur, add_stud_num, add_skills)
