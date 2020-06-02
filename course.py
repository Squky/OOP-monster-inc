class Course():

    def __init__(self,mod_name,list_of_students,start_date):
        self.course_name = mod_name,
        self.student_list = list_of_students,
        self.course_start = start_date


    def add_student(self,student):
        self.student_list.append(student)