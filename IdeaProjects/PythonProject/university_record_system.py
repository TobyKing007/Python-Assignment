OFFICIAL_COURSES = {
    "Math", "Physics", "Computer Science", "Biology", "Chemistry",
    "Statistics", "English", "Economics", "History", "Philosophy",
    "Sociology", "Political Science", "Geography", "Psychology",
    "Art", "Music", "Engineering", "Law", "Medicine", "Business"
}

def student_count(students):
    return len(students)

def create_student_record(name, age, courses, address):
    return {"name": name, "age": age, "courses": courses, "address": address}

def add_student(students, username, name, age, courses, address):
    if username in students:
        return False
    students[username] = create_student_record(name, age, courses, address)
    return True

def get_student_record(students, username):
    if username in students:
        return students[username]

    return None

def get_student_courses(students, username):
    if username in students:
        return students[username]["courses"]
    return None

def get_student_zip_code(students, username):
    if username in students:
        return students[username]["address"]["zip_code"]
    return None

def get_student_city_address(students, username):
    if username in students:
        return students[username]["address"]["city"]
    return None