import psycopg2

class StudentModel:
    # Hàm tạo kết nối đến cơ sở dữ liệu, với tham số tùy chỉnh cho kết nối
    @staticmethod
    def database_connection(host, user, password, database):
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            return connection
        except Exception as e:
            raise Exception(f"Lỗi kết nối cơ sở dữ liệu: {str(e)}")

    @staticmethod
    def get_all_students(host, user, password, database):
        try:
            connection = StudentModel.database_connection(host, user, password, database)  
            curs = connection.cursor()
            curs.execute("SELECT * FROM student_register")
            rows = curs.fetchall() # fetchall() lấy tất cả các kết quả trả về từ một truy vấn db
            connection.close()
            return rows
        except Exception as e:
            raise Exception(f"Lỗi khi tải danh sách sinh viên: {str(e)}")

    @staticmethod
    def search_student_by_phone(phone, host, user, password, database):
        try:
            connection = StudentModel.database_connection(host, user, password, database)  
            curs = connection.cursor()
            curs.execute("SELECT * FROM student_register WHERE contact = %s", (phone,))
            row = curs.fetchone()
            connection.close()
            return row
        except Exception as e:
            raise Exception(f"Lỗi khi tìm sinh viên: {str(e)}")

    @staticmethod
    def add_student(student_data, host, user, password, database):
        try:
            connection = StudentModel.database_connection(host, user, password, database)  
            curs = connection.cursor()
            curs.execute("""
                INSERT INTO student_register (f_name, l_name, course, subject, year, age, gender, birth, contact, email) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, student_data)
            connection.commit()
            connection.close()
        except Exception as e:
            raise Exception(f"Không thể thêm sinh viên: {str(e)}")

    @staticmethod
    def update_student(student_data, phone, host, user, password, database):
        try:
            connection = StudentModel.database_connection(host, user, password, database)  
            curs = connection.cursor()
            curs.execute("""
                UPDATE student_register 
                SET f_name=%s, l_name=%s, course=%s, subject=%s, year=%s, age=%s, gender=%s, birth=%s, email=%s 
                WHERE contact=%s
            """, student_data + (phone,))
            connection.commit()
            connection.close()
        except Exception as e:
            raise Exception(f"Lỗi khi cập nhật sinh viên: {str(e)}")

    @staticmethod
    def delete_student(phone, host, user, password, database):
        try:
            connection = StudentModel.database_connection(host, user, password, database)  
            curs = connection.cursor()
            curs.execute("DELETE FROM student_register WHERE contact=%s", (phone,))
            connection.commit()
            connection.close()
        except Exception as e:
            raise Exception(f"Lỗi khi xóa sinh viên: {str(e)}")
