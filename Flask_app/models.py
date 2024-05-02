from flask import redirect, url_for

# ? Auth
from flask_login import UserMixin, current_user
from __init__ import my_login_manager

# ? DB
from __init__ import my_db


# ? Admin Dashboard
from flask_admin.contrib.sqla import ModelView
from __init__ import my_admin


ADMIN = ["admin"]  # ?List of users who can access the /admin page


# ?DB for /admin
class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.username in ADMIN

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("login", next=request.url))


# ?------- OUR Tables   --------


#! Users Table
class User(my_db.Model, UserMixin):
    "User Model - Teacher or Student"
    __tablename__ = "users"

    column_list = (
        "username",
        "password",
        "email",
        "full_name",
        "profile_pic_url",
        "role",
    )

    username = my_db.Column(my_db.String, primary_key=True, nullable=False)
    password = my_db.Column(my_db.String, nullable=False)
    email = my_db.Column(my_db.String)

    full_name = my_db.Column(my_db.String, nullable=False)

    profile_pic_url = my_db.Column(my_db.String, nullable=False, default="default.jpg")

    role = my_db.Column(my_db.String, nullable=False)  # ? student or teacher

    def __repr__(self):
        return f"User(username = {self.username}, password = {self.password}, email = {self.email}, full_name = {self.full_name}, role={self.role})"

    def get_id(self):
        return self.username


# ?Callback - Manage user Authentication and Session persistence
@my_login_manager.user_loader
def laod_user(username):
    return User.query.get(username)


#! Courses Table
class Course(my_db.Model):
    """Course model represents a course offered on the platform, taught by a teacher.
    
    teacher_username: Foreign key referencing the username of the teacher (User).
    teacher: Relationship to User model, specifying the teacher of the course.
      > This relationship indicates that each course is associated with a specific user (teacher) who is responsible for teaching the course.
    
    students: Many-to-many relationship with User model through Enrollment association table, 
     representing students enrolled in the course.
    """
    
    __tablename__ = "courses"

    id = my_db.Column(my_db.Integer, primary_key=True)
    title = my_db.Column(my_db.String(100), nullable=False)
    description = my_db.Column(my_db.Text, nullable=False)
    teacher_id = my_db.Column(
        my_db.String, my_db.ForeignKey("users.username"), nullable=False
    )
    teacher = my_db.relationship(
        "User", backref="courses_taught", foreign_keys=[teacher_id]
    )
    students = my_db.relationship(
        "User", secondary="enrollments", backref="courses_enrolled"
    )

    def __repr__(self):
        return f"Course(id={self.id}, title='{self.title}', description='{self.description}', teacher_id={self.teacher_id}, teacher={self.teacher}, students={self.students})"


#! Enrollments Table
class Enrollment(my_db.Model):
    """Enrollment model manages the relationship between courses and students.
    
    Each Enrollment record represents a student's enrollment in a course (course_id) 
    and specifies the student (student_id) and their role (role) in the course (typically 'student').
    
    course_id: Foreign key referencing the id of the course (Course).
    student_username: Foreign key referencing the username of the student (User).
    status: Status of the enrollment, e.g., 'Enrolled', 'In Progress', 'Completed'.
    created_at: Timestamp of when the enrollment was created.
    
    student: Relationship to User model, specifying the student enrolled in the course.
    """

    __tablename__ = "enrollments"

    course_id = my_db.Column(my_db.Integer, my_db.ForeignKey("courses.id"), primary_key=True)
    student_id = my_db.Column(my_db.String, my_db.ForeignKey("users.username"), primary_key=True)
    status = my_db.Column(my_db.String)  # Add the 'status' field
    created_at = my_db.Column(my_db.Timestamp, default=my_db.func.now())

    # Define relationship to User model for the student
    student = my_db.relationship("User", backref="enrollments")

    def __repr__(self):
        return f"Enrollment(course_id={self.course_id}, student_id='{self.student_id}', student={self.student}, status='{self.status}, created_at={self.created_at})"


# ?Generating an /admin UI for all the tables
all_models = [User, Course, Enrollment]
for model in all_models:
    my_admin.add_view(MyModelView(model, my_db.session))


# TODO:
#! Validation and Error Handling: Implement validation for the role attribute to ensure it accepts only valid roles (e.g., 'Teacher' or 'Student').

#! Security: Always use secure practices for handling user passwords (e.g., hashing and salting) to protect user credentials.

#! User Interface: Update the user interface (e.g., templates, forms) to accommodate the new user attributes and role selection during user registration or profile updates.
