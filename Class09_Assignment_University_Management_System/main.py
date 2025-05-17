# -----------------------------------------------------------------------------
# Person: Base class that provides common attributes for all university members
# -----------------------------------------------------------------------------
class Person:
    def __init__(self, name, age):
        # Initialize basic personal information
        self.name = name  # Full name of the person
        self.age = age    # Age of the person
    
    def getName(self):
        # Returns formatted string containing person's details
        return f"Name: {self.name}, Age: {self.age}"

# -----------------------------------------------------------------------------
# Student: Represents a student in the university system
# -----------------------------------------------------------------------------
class Student(Person):
    def __init__ (self, name, age, roll_number) -> None:
        super(). __init__(name, age)
        self.roll_number:str = roll_number  # Unique student identification number
        self.course = []                    # Track enrolled courses
    
    def registerForCourse(self, course):
        # Handles student course registration and updates course roster
        if course not in self.course:
            self.course.append(course)
            course.add_student(self)

# -----------------------------------------------------------------------------
# Instructor: Represents a faculty member in the university
# -----------------------------------------------------------------------------
class Instructor(Person):
    def __init__(self, name, age, salary) -> None:
        super(). __init__(name, age)
        self.salary = salary    # Instructor's compensation
        self.courses = []       # Courses being taught
    
    def assign_course(self, course):
        # Links instructor to a course and updates course information
        if course not in self.courses:
            self.courses.append(course)
            course.set_instructor(self)

# -----------------------------------------------------------------------------
# Course: Manages course-related information and relationships
# -----------------------------------------------------------------------------
class Course:
    def __init__ (self, id, name) -> None:
        self.id = id                # Course code/identifier
        self.name = name            # Course title
        self.students = []          # Enrolled students list
        self.instructor = None      # Assigned instructor
    
    def add_student(self, student):
        # Enrolls a student in the course
        if student not in self.students:
            self.students.append(student)
    
    def set_instructor(self, instructor):
        # Assigns an instructor to the course
        self.instructor = instructor

# -----------------------------------------------------------------------------
# Department: Organizes courses under academic departments
# -----------------------------------------------------------------------------
class Department:
    def __init__(self, name) -> None:
        self.name = name        # Department name
        self.courses = []       # Available courses
    
    def add_course(self, course):
        # Adds a course to department's offerings
        if course not in self.courses:
            self.courses.append(course)

# -----------------------------------------------------------------------------
# University: Top-level management class for the entire system
# -----------------------------------------------------------------------------
class University:
    def __init__(self, name) -> None:
        self.name = name            # University name
        self.departments = []       # List of departments
    
    def add_department(self, department):
        # Adds a new department to the university
        if department not in self.departments:
            self.departments.append(department)

# -----------------------------------------------------------------------------
# Example Usage and System Implementation
# -----------------------------------------------------------------------------

# Initialize university
uni = University("Tech University")

# Set up departments
cs_depart = Department("Computer Science")
math_dept = Department("Mathematics")

uni.add_department(cs_depart)
uni.add_department(math_dept)

# Create course offerings
ai_course = Course("AI101", "Artificial Intelligence")
ml_course = Course("ML201", "Machine Learning")

cs_depart.add_course(ai_course)
cs_depart.add_course(ml_course)

# Set up faculty
instructor1 = Instructor("Dr. Smith", 45, 50000)
instructor1.assign_course(ai_course)

# Register students
student1 = Student("Alice", 20, "GIAIC1234")
student2 = Student("Osama", 36, "GIAIC5678")

student1.registerForCourse(ai_course)
student2.registerForCourse(ai_course)

# Output course enrollment information
print(f"Course: {ai_course.name}")
for student in ai_course.students:
    print(f"- {student.name} ({student.roll_number})")

# Display course instructor
if ai_course.instructor:
    print(f"Instructor: {ai_course.instructor.name}")