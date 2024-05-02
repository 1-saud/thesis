from Flask_app import my_db

#? Models 
from Flask_app.models import User, Course, Enrollment


#! User test
def test_user():
    # Registering a new user
    new_user = User(
        username="john_doe",
        password="password123",
        email="john@example.com",
        full_name="John Doe",
        profile_pic_url="profile.jpg",
        role="Student",
    )
    my_db.session.add(new_user)
    my_db.session.commit()
    
    
def display_users():
    # Retrieve all users from the database
    users = User.query.all()
    
    # Display information about each user
    for user in users:
        print(f"Username: {user.username}")
        print(f"Full Name: {user.full_name}")
        print(f"Email: {user.email}")
        print(f"Profile Picture URL: {user.profile_pic_url}")
        print(f"Role: {user.role}")
        print("\n")
    
    
#! Course test    
def test_courses():
    # Create some sample courses
    course1 = Course(title="Mathematics", description="Introductory Mathematics Course", teacher_id="teacher1")
    course2 = Course(title="Physics", description="Physics for Beginners", teacher_id="teacher2")
    course3 = Course(title="Biology", description="Basic Biology Concepts", teacher_id="teacher3")
    
    # Add courses to the session
    my_db.session.add(course1)
    my_db.session.add(course2)
    my_db.session.add(course3)
    
    # Commit the changes to the database
    my_db.session.commit()

def display_courses():
    # Retrieve all courses from the database
    courses = Course.query.all()
    
    # Display information about each course
    for course in courses:
        print(f"Course ID: {course.id}")
        print(f"Title: {course.title}")
        print(f"Description: {course.description}")
        print(f"Teacher ID: {course.teacher_id}")
        print(f"Teacher: {course.teacher}")
        print(f"Students Enrolled: {course.students}")
        print("\n")
        

#! Enrolments test    
def test_enrollments():
    # Create some sample enrollments (students enrolling in courses)
    enrollment1 = Enrollment(course_id=1, student_id="student1", role="Student")
    enrollment2 = Enrollment(course_id=1, student_id="student2", role="Student")
    enrollment3 = Enrollment(course_id=2, student_id="student3", role="Student")
    
    # Add enrollments to the session
    my_db.session.add(enrollment1)
    my_db.session.add(enrollment2)
    my_db.session.add(enrollment3)
    
    # Commit the changes to the database
    my_db.session.commit()

def display_enrollments():
    # Retrieve all enrollments from the database
    enrollments = Enrollment.query.all()
    
    # Display information about each enrollment
    for enrollment in enrollments:
        print(f"Course ID: {enrollment.course_id}")
        print(f"Student ID: {enrollment.student_id}")
        print(f"Student: {enrollment.student}")
        print(f"Role: {enrollment.role}")
        print("\n")



#!  ----- Run tests -----
if __name__ == "__main__":
    print("----- Testing: All Models -----")

    #? test users
    print("----- Testing: User Models -----")
    test_user()
    
    # Display information about all users
    print("List of Users:")
    display_users()
    
    # Display information about a specific user
    # Checking user's role
    print("----- Testing: Checking user's role -----")
    user = User.query.filter_by(username="john_doe").first()
    if user.role == "Student":
        print(f"{user.username} is a student.")
    elif user.role == "Teacher":
        print(f"{user.username} is a teacher.")
    else:
        print(f"{user.username} has an unknown role.")
    
    
    #? test courses
    print("----- Testing: Courses Models -----")
    test_courses()
    
    # Display information about all courses
    print("List of Courses:")
    display_courses()
    
    
    #? test enrollments
    print("----- Testing: Enrollments Models -----")
    test_enrollments()
    
    # Display information about all enrollments
    print("List of Enrollments:")
    display_enrollments()