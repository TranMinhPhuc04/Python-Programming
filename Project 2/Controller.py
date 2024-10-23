from Model import StudentModel

class StudentController:
    def __init__(self, host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname

    @staticmethod
    def login(username, password):
        try:
            # Kết nối đến cơ sở dữ liệu bằng phương thức từ StudentModel
            conn = StudentModel.database_connection()

            # Kiểm tra tài khoản người dùng
            user = StudentModel.verify_user_credentials(conn, username, password)

            if user:
                # Trả về kết nối nếu đăng nhập thành công
                return conn
            else:
                raise Exception("Tên người dùng hoặc mật khẩu không hợp lệ")

        except Exception as e:
            raise Exception(f"Lỗi đăng nhập: {str(e)}")


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
