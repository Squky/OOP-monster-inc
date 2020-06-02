
from student_monster import *


Sulley = Student("Sulley",1234,"green",4321,["Loud Roar"]) 

print(Sulley.get_student())


Sulley.add_skills("Expert in Hand-to-hand combat")

print(Sulley.skills)

# ///////////////////////////
# The code below allows the user to generate a student from their own inputs


# student_instance = Student
#
# student_instance.set_student(Student) # Running this function asks for the users input in creating the student. (e.g. 'name', 'fur')
#
# student_instance.get_student(Student) # Returns That newly created student instance in a formatted way