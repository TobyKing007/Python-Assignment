import unittest

from university_record_system import *


class UniversityRecordSystemTest(unittest.TestCase):

    def test_dictionary_is_empty(self):
        students = {}

        result = student_count(students)

        self.assertEqual(result, 0)

    def test_dictionary_length_becomes_one_when_a_student_is_added(self):
        students = { "jp101" : dict(name="Jonathan Pascal", age=18, courses={"Math", "Physics"},
                                    address={"city": "Lagos", "zip_code": "100001"})

        }
        result = student_count(students)
        self.assertEqual(result, 1)

    def test_that_the_create_function_creates_a_student_record(self):
        student_info = create_student_record(name="Jonathan Pascal", age=18, courses={"Math", "Physics"},address={"city": "Lagos", "zip_code": "100001"})

        self.assertEqual(student_info["name"], "Jonathan Pascal")
        self.assertEqual(student_info["age"], 18)
        self.assertEqual(student_info["courses"], {"Math", "Physics"})
        self.assertEqual(student_info["address"], {"city": "Lagos", "zip_code": "100001"})

    def test_that_student_can_be_added_to_dictionary(self):
        students = {}
        add_student(students, "jp101", "Jonathan Pascal", 18, {"Math", "Physics"}, {"city": "Lagos", "zip_code": "100001"})
        self.assertIn("jp101", students)
        self.assertEqual(students["jp101"]["name"], "Jonathan Pascal")
        self.assertEqual(students["jp101"]["age"], 18)
        self.assertEqual(students["jp101"]["courses"], {"Math", "Physics"})
        self.assertEqual(students["jp101"]["address"], {"city": "Lagos", "zip_code": "100001"})

    def test_that_new_student_cannot_be_added_with_existing_username(self):
        students = {}
        add_student(students, "jp101", "Jonathan Pascal", 18, {"Math", "Physics"},
                    {"city": "Lagos", "zip_code": "100001"})

        result = add_student(students, "jp101", "Adebola Mayowa", 17, {"Math", "chemistry"}, {"city": "Abuja", "zip_code": "900001"})
        self.assertFalse(result)
        self.assertEqual(students["jp101"]["name"], "Jonathan Pascal")

    def test_that_get_student_record_function_can_get_student_record(self):
        students = {}
        add_student(students, "jp101", "Jonathan Pascal", 18, {"Math", "Physics"},
                    {"city": "Lagos", "zip_code": "100001"})

        result = get_student_record(students, "jp101")
        self.assertEqual(result["name"], "Jonathan Pascal")
        self.assertEqual(result["age"], 18)
        self.assertEqual(result["courses"], {"Math", "Physics"})
        self.assertEqual(result["address"], {"city": "Lagos", "zip_code": "100001"})

    def test_that_function_returns_null_if_username_is_not_found(self):
        students = {}
        result = get_student_record(students, "jp101")
        self.assertIsNone(result)

    def test_that_get_student_courses_function__returns_student_courses(self):
        students = {}

        add_student(students, "jp101", "Jonathan Pascal", 18, {"Math", "Physics"},
                    {"city": "Lagos", "zip_code": "100001"})

        result = get_student_courses (students, "jp101")
        self.assertEqual(result, {"Math", "Physics"})

    def test_that_get_student_zip_code_returns_student_zip_code(self):
        students = {}

        add_student(students, "jp101", "Jonathan Pascal", 18, {"Math", "Physics"},
                    {"city": "Lagos", "zip_code": "100001"})

        result = get_student_zip_code(students, "jp101")
        self.assertEqual(result, "100001")

    def test_that_get_student_address_returns_student_city_address (self):
        students = {}

        add_student(students, "jp101", "Jonathan Pascal", 18, {"Math", "Physics"},
                    {"city": "Lagos", "zip_code": "100001"})

        result = get_student_city_address(students, "jp101")
        self.assertEqual(result, "Lagos")

        def test_that_student_function_can_add_a_new_course (self):
            students = {}
            add_student(students, "jp101", "Jonathan Pascal", 18, {"Math", "Physics"},
                    {"city": "Lagos", "zip_code": "100001"})

            result = 

