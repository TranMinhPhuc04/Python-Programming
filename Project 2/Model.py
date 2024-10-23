import psycopg2
class StudentModel:
    @staticmethod
    def database_connection():
        try:
            connection = psycopg2.connect(
                host='127.0.0.1',  
                user='postgres',    
                password='123456',  
                dbname='student_management'  
            )
            return connection
        except Exception as e:
            raise Exception(f"Lỗi kết nối cơ sở dữ liệu: {str(e)}")

    @staticmethod
    def verify_user_credentials(connection, username, password):
        try:
            with connection.cursor() as curs:
                curs.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
                user = curs.fetchone()
                return user
        except Exception as e:
            raise Exception(f"Lỗi khi kiểm tra thông tin đăng nhập: {str(e)}")
    @staticmethod
    def get_all_students(connection):
        try:
            with connection.cursor() as curs:
                curs.execute("SELECT * FROM student_register")
                rows = curs.fetchall()
            return rows
        except Exception as e:
            raise Exception(f"Lỗi khi tải danh sách sinh viên: {str(e)}")

    @staticmethod
    def search_student_by_phone(connection, phone):
        try:
            with connection.cursor() as curs:
                curs.execute("SELECT * FROM student_register WHERE contact = %s", (phone,))
                row = curs.fetchone()
            return row
        except Exception as e:
            raise Exception(f"Lỗi khi tìm sinh viên: {str(e)}")

    @staticmethod
    def add_student(connection, student_data):
        try:
            with connection.cursor() as curs:
                curs.execute("""
                    INSERT INTO student_register (f_name, l_name, course, subject, year, age, gender, birth, contact, email) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, student_data)
                connection.commit()
        except Exception as e:
            connection.rollback()  # Rollback in case of an error
            raise Exception(f"Không thể thêm sinh viên: {str(e)}")

    @staticmethod
    def update_student(connection, student_data, phone):
        try:
            with connection.cursor() as curs:
                curs.execute("""
                    UPDATE student_register 
                    SET f_name=%s, l_name=%s, course=%s, subject=%s, year=%s, age=%s, gender=%s, birth=%s, email=%s 
                    WHERE contact=%s
                """, student_data + (phone,))
                connection.commit()
        except Exception as e:
            connection.rollback()
            raise Exception(f"Lỗi khi cập nhật sinh viên: {str(e)}")

    @staticmethod
    def delete_student(connection, phone):
        try:
            with connection.cursor() as curs:
                curs.execute("DELETE FROM student_register WHERE contact=%s", (phone,))
                connection.commit()
        except Exception as e:
            connection.rollback()
            raise Exception(f"Lỗi khi xóa sinh viên: {str(e)}")
