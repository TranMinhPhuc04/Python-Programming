from Model import StudentModel
import psycopg2

class StudentController:
    def __init__(self, host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname

    @staticmethod
    def login(username, password):
        try:
            # Kết nối đến cơ sở dữ liệu
            conn = psycopg2.connect(
                host='127.0.0.1',  
                user='postgres',    
                password='123456',  
                dbname='student_management'  
            )
            # Trả về kết nối cơ sở dữ liệu nếu kết nối thành công
            return conn
        except Exception as e:
            # Xử lý lỗi khi kết nối đến cơ sở dữ liệu
            raise Exception(f"Lỗi kết nối: {str(e)}")

    def get_all_students(self, connection):
        return StudentModel.get_all_students(connection)

    def search_student_by_phone(self, connection, phone):
        return StudentModel.search_student_by_phone(connection, phone)

    def add_student(self, connection, student_data):
        StudentModel.add_student(connection, student_data)

    def update_student(self, connection, student_data, phone):
        StudentModel.update_student(connection, student_data, phone)

    def delete_student(self, connection, phone):
        StudentModel.delete_student(connection, phone)
