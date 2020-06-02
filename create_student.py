
from student_monster import *
from create_course import *
# Create some students
Sulley = Student("Sulley",1234,"green",4321,["Loud Roar"])

Mike = Student("Mike",6789,"No Fur",9876,["Lound and obnoxious","Expert in complaining"])

# Add/update their attributes
Sulley.add_skills("Expert in Hand-to-hand combat")
Mike.add_skills("Hiding behind logos")
Mike.set_fur("Some Fur?")

# Display the students and their attributes
print(Sulley.get_student())
print(Mike.get_student())


print(course1.add_student(Mike))
print(course1.add_student(Sulley))
#print(course1.student_list,'\n')  # Prints the student list for course1


# This calls the 'get_course()' method which prints out the details of the given Course object
course1.get_course()


# Uses a function to print the student list instead
print(course1.get_students())

# ///////////////////////////
# The code below allows the user to generate a student from their own inputs


# student_instance = Student
#
# student_instance.set_student(Student) # Running this function asks for the users input in creating the student. (e.g. 'name', 'fur')
#
# student_instance.get_student(Student) # Returns That newly created student instance in a formatted way