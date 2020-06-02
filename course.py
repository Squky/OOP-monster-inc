class Course():

    def __init__(self,mod_name,start_date,list_of_students=[]):
        self.course_name = mod_name
        self.student_list = list_of_students
        self.course_start = start_date


    def add_student(self,student):
        self.student_list.append(student.name)
        return f"{student.name} added as a new student!"


    # This method displys the course and its attributes in a formatted style using a dictionary
    def get_course(self):
        courses={

            "Course Name                ": self.course_name,
            "Start Date                 ": self.course_start,
            "Students enrolled on Course": self.student_list

        }

        for i in courses:
            print(i, " : ", courses[i])