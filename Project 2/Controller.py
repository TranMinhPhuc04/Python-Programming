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
            cursor = conn.cursor()
            
            # Thực hiện truy vấn kiểm tra tài khoản người dùng
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            result = cursor.fetchone()  # Trả về kết quả nếu tìm thấy tài khoản
            conn.close()
            return result
        except Exception as e:
            # Xử lý lỗi khi kết nối đến cơ sở dữ liệu hoặc truy vấn
            raise Exception(f"Lỗi kết nối: {str(e)}")


    def get_all_students(self):
        return StudentModel.get_all_students(self.host, self.user, self.password, self.dbname)

    def search_student_by_phone(self, phone):
        return StudentModel.search_student_by_phone(phone, self.host, self.user, self.password, self.dbname)

    def add_student(self, student_data):
        StudentModel.add_student(student_data, self.host, self.user, self.password, self.dbname)

    def update_student(self, student_data, phone):
        StudentModel.update_student(student_data, phone, self.host, self.user, self.password, self.dbname)

    def delete_student(self, phone):
        StudentModel.delete_student(phone, self.host, self.user, self.password, self.dbname)
