OFFICIAL_COURSES = {
    "Math", "Physics", "Computer Science", "Biology", "Chemistry",
    "Statistics", "English", "Economics", "History", "Philosophy",
    "Sociology", "Political Science", "Geography", "Psychology",
    "Art", "Music", "Engineering", "Law", "Medicine", "Business"
}

students = {}


def create_student(username, name, age, courses, city, zip_code):
    if username in students:
        return "Username already exists."

    valid_courses = set()

    for course in courses:
        if course in OFFICIAL_COURSES:
            valid_courses.add(course)

    students[username] = {
        "name": name,
        "age": age,
        "courses": valid_courses,
        "address": {
            "city": city,
            "zip_code": zip_code
        }
    }

    return "Student record created successfully."


def display_student_record(username):
    if username not in students:
        return "Student not found."
    return students[username]


def display_student_courses(username):
    if username not in students:
        return "Student not found."
    return students[username]["courses"]


def display_student_zip_code(username):
    if username not in students:
        return "Student not found."
    return students[username]["address"]["zip_code"]


def display_student_city(username):
    if username not in students:
        return "Student not found."
    return students[username]["address"]["city"]


def add_course(username, new_course):
    if username not in students:
        return "Student not found."

    if new_course not in OFFICIAL_COURSES:
        return "Course not officially offered."

    if new_course in students[username]["courses"]:
        return "Course already exists."

    students[username]["courses"].add(new_course)
    return "Course added successfully."


def remove_course(username, course):
    if username not in students:
        return "Student not found."

    if course not in students[username]["courses"]:
        return "Course not found."

    students[username]["courses"].remove(course)
    return "Course removed successfully."


def update_course(username, old_course, new_course):
    if username not in students:
        return "Student not found."

    if old_course not in students[username]["courses"]:
        return "Old course not found."

    if new_course not in OFFICIAL_COURSES:
        return "New course not officially offered."

    if new_course in students[username]["courses"]:
        return "Course already exists."

    students[username]["courses"].remove(old_course)
    students[username]["courses"].add(new_course)

    return "Course updated successfully."


def update_student_details(username, new_name=None, new_age=None, new_city=None, new_zip_code=None):
    if username not in students:
        return "Student not found."

    if new_name is not None:
        students[username]["name"] = new_name

    if new_age is not None:
        students[username]["age"] = new_age

    if new_city is not None:
        students[username]["address"]["city"] = new_city

    if new_zip_code is not None:
        students[username]["address"]["zip_code"] = new_zip_code

    return "Student details updated successfully."


def display_total_students():
    return len(students)



