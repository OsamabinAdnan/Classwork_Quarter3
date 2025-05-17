# University Management System

A simple Python-based university management system that models the relationships between university entities including students, instructors, courses, and departments.

## Features

- Object-oriented design with inheritance
- Management of university hierarchy:
  - University contains departments
  - Departments offer courses
  - Courses have instructors and students
  - Students can register for courses
  - Instructors can be assigned to courses

## Class Structure

- `Person`: Base class for people in the university system
- `Student`: Inherits from Person, manages course enrollment
- `Instructor`: Inherits from Person, manages course assignments
- `Course`: Manages course details, students, and instructor
- `Department`: Manages a collection of courses
- `University`: Top-level class managing departments

## Usage Example

```python
# Create university instance
uni = University("Tech University")

# Create and add departments
cs_depart = Department("Computer Science")
uni.add_department(cs_depart)

# Create and add courses
ai_course = Course("AI101", "Artificial Intelligence")
cs_depart.add_course(ai_course)

# Create and assign instructor
instructor1 = Instructor("Dr. Smith", 45, 50000)
instructor1.assign_course(ai_course)

# Create and enroll students
student1 = Student("Alice", 20, "GIAIC1234")
student1.registerForCourse(ai_course)

# Display course information
print(f"Course: {ai_course.name}")
for student in ai_course.students:
    print(f"- {student.name} ({student.roll_number})")
```

## Requirements

- Python 3.6 or higher
- No external dependencies

## License

This project is available under the MIT License.