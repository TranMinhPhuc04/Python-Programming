from Model import StudentModel
import psycopg2

class StudentController:
    def __init__(self):
        pass

    @staticmethod
    def login(username, password):
        try:
            conn = psycopg2.connect(
                host='127.0.0.1',
                user='postgres',
                password='123456',
                dbname='student_management'
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            result = cursor.fetchone()
            conn.close()
            return result
        except Exception as e:
            raise Exception(f"Lỗi kết nối: {str(e)}")

    @staticmethod
    def get_all_students():
        return StudentModel.get_all_students()

    @staticmethod
    def search_student_by_phone(phone):
        return StudentModel.search_student_by_phone(phone)

    @staticmethod
    def add_student(student_data):
        StudentModel.add_student(student_data)

    @staticmethod
    def update_student(student_data, phone):
        StudentModel.update_student(student_data, phone)

    @staticmethod
    def delete_student(phone):
        StudentModel.delete_student(phone)
