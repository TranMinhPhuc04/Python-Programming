import psycopg2

class StudentModel:
    @staticmethod
    def get_all_students():
        try:
            connection = psycopg2.connect(host='127.0.0.1', user='postgres', password='123456', database='student_management')
            curs = connection.cursor()
            curs.execute("SELECT * FROM student_register")
            rows = curs.fetchall()
            connection.close()
            return rows
        except Exception as e:
            raise Exception(f"Lỗi khi tải danh sách sinh viên: {str(e)}")

    @staticmethod
    def search_student_by_phone(phone):
        try:
            connection = psycopg2.connect(host='127.0.0.1', user='postgres', password='123456', database='student_management')
            curs = connection.cursor()
            curs.execute("SELECT * FROM student_register WHERE contact = %s", (phone,))
            row = curs.fetchone()
            connection.close()
            return row
        except Exception as e:
            raise Exception(f"Lỗi khi tìm sinh viên: {str(e)}")

    @staticmethod
    def add_student(student_data):
        try:
            connection = psycopg2.connect(host='127.0.0.1', user='postgres', password='123456', database='student_management')
            curs = connection.cursor()
            curs.execute("INSERT INTO student_register (f_name, l_name, course, subject, year, age, gender, birth, contact, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                         student_data)
            connection.commit()
            connection.close()
        except Exception as e:
            raise Exception(f"Không thể thêm sinh viên: {str(e)}")

    @staticmethod
    def update_student(student_data, phone):
        try:
            connection = psycopg2.connect(host='127.0.0.1', user='postgres', password='123456', database='student_management')
            curs = connection.cursor()
            curs.execute("""
                UPDATE student_register 
                SET f_name=%s, l_name=%s, course=%s, subject=%s, year=%s, age=%s, gender=%s, birth=%s, email=%s 
                WHERE contact=%s
                """,
                student_data + (phone,))
            connection.commit()
            connection.close()
        except Exception as e:
            raise Exception(f"Lỗi khi cập nhật sinh viên: {str(e)}")

    @staticmethod
    def delete_student(phone):
        try:
            connection = psycopg2.connect(host='127.0.0.1', user='postgres', password='123456', database='student_management')
            curs = connection.cursor()
            curs.execute("DELETE FROM student_register WHERE contact=%s", (phone,))
            connection.commit()
            connection.close()
        except Exception as e:
            raise Exception(f"Lỗi khi xóa sinh viên: {str(e)}")
        
    @staticmethod
    def get_all_students():
        try:
            connection = psycopg2.connect(host='127.0.0.1', user='postgres', password='123456', database='student_management')
            curs = connection.cursor()
            curs.execute("SELECT * FROM student_register")
            rows = curs.fetchall()
            connection.close()
            return rows
        except Exception as e:
            raise Exception(f"Lỗi khi tải danh sách sinh viên: {str(e)}")

