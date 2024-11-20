from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Student, Course, Enrollment
from app.utils import login_required  # Import decorator từ utils.py
from datetime import date

bp = Blueprint('student', __name__)


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        mssv = request.form.get('mssv')
        name = request.form.get('name')
        email = request.form.get('email')
        major = request.form.get('major')

        if not mssv or not name or not email:
            flash('MSSV, Name và Email là bắt buộc!', 'danger')
        elif Student.query.get(mssv):
            flash('MSSV đã tồn tại!', 'danger')
        else:
            new_student = Student(mssv=mssv, name=name,
                                  email=email, major=major)
            db.session.add(new_student)
            db.session.commit()
            flash('Thêm sinh viên thành công!', 'success')

    students = Student.query.all()
    return render_template('index.html', students=students)


@bp.route('/delete/<mssv>', methods=['POST'])
@login_required
def delete_student(mssv):
    student = Student.query.get(mssv)
    if not student:
        flash('Không tìm thấy sinh viên!', 'danger')
    else:
        if student.enrollments:  # Kiểm tra xem sinh viên có đăng ký môn học không
            flash('Không thể xóa sinh viên vì đã đăng ký môn học!', 'danger')
        else:
            db.session.delete(student)
            db.session.commit()
            flash('Xóa sinh viên thành công!', 'success')

    return redirect(url_for('student.index'))


@bp.route('/edit/<mssv>', methods=['GET', 'POST'])
@login_required
def edit_student(mssv):
    student = Student.query.get(mssv)
    if not student:
        flash('Không tìm thấy sinh viên!', 'danger')
        return redirect(url_for('student.index'))

    if request.method == 'POST':
        student.name = request.form.get('name')
        student.email = request.form.get('email')
        student.major = request.form.get('major')
        db.session.commit()
        flash('Cập nhật thông tin sinh viên thành công!', 'success')
        return redirect(url_for('student.index'))

    students = Student.query.all()
    return render_template('index.html', students=students, editing_student=student)


# Quản lý Môn học


@bp.route('/courses', methods=['GET', 'POST'])
@login_required
def courses():
    editing_course = None  # Biến lưu trữ thông tin môn học đang chỉnh sửa

    if request.method == 'POST':
        # Lấy course_id nếu đang chỉnh sửa
        course_id = request.form.get('course_id')
        course_name = request.form.get('course_name')
        credits = request.form.get('credits')

        if not course_name or not credits:
            flash('Tên môn học và số tín chỉ là bắt buộc!', 'danger')
        else:
            try:
                credits = int(credits)  # Chuyển đổi số tín chỉ sang kiểu số
                if credits <= 0:  # Kiểm tra nếu số tín chỉ <= 0
                    flash('Số tín chỉ phải lớn hơn 0!', 'danger')
                elif course_id:  # Nếu có course_id, thực hiện chỉnh sửa
                    course = Course.query.get(course_id)
                    if course:
                        course.course_name = course_name
                        course.credits = credits
                        db.session.commit()
                        flash('Cập nhật môn học thành công!', 'success')
                    else:
                        flash('Không tìm thấy môn học!', 'danger')
                else:  # Nếu không có course_id, thêm mới môn học
                    new_course = Course(
                        course_name=course_name, credits=credits)
                    db.session.add(new_course)
                    db.session.commit()
                    flash('Thêm môn học thành công!', 'success')
            except ValueError:
                flash('Số tín chỉ phải là số nguyên!', 'danger')

        return redirect(url_for('student.courses'))

    # Kiểm tra nếu có yêu cầu chỉnh sửa
    edit_id = request.args.get('edit_id')
    if edit_id:
        editing_course = Course.query.get(edit_id)

    courses = Course.query.all()
    return render_template('courses.html', courses=courses, editing_course=editing_course)


@bp.route('/delete_course/<int:course_id>', methods=['POST'])
@login_required
def delete_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        flash('Không tìm thấy môn học!', 'danger')
    else:
        if course.enrollments:
            flash('Không thể xóa môn học vì đã có sinh viên đăng ký!', 'danger')
        else:
            db.session.delete(course)
            db.session.commit()
            flash('Xóa môn học thành công!', 'success')

    return redirect(url_for('student.courses'))

# Đăng ký Môn học


@bp.route('/enrollments', methods=['GET', 'POST'])
@login_required
def enrollments():
    students = Student.query.all()
    courses = Course.query.all()

    if request.method == 'POST':
        student_mssv = request.form.get('student_mssv')
        course_id = request.form.get('course_id')

        if not student_mssv or not course_id:
            flash('Vui lòng chọn sinh viên và môn học!', 'danger')
        else:
            existing_enrollment = Enrollment.query.filter_by(
                student_mssv=student_mssv, course_id=course_id).first()
            if existing_enrollment:
                flash('Sinh viên đã đăng ký môn học này rồi!', 'danger')
            else:
                new_enrollment = Enrollment(
                    student_mssv=student_mssv, course_id=course_id, enrollment_date=date.today())
                db.session.add(new_enrollment)
                db.session.commit()
                flash('Đăng ký môn học thành công!', 'success')

    enrollments = Enrollment.query.all()
    return render_template('enrollments.html', enrollments=enrollments, students=students, courses=courses)


# Hủy đăng ký Môn học


@bp.route('/unenroll/<int:enrollment_id>', methods=['POST'])
@login_required
def unenroll(enrollment_id):
    enrollment = Enrollment.query.get(enrollment_id)
    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()
        flash('Hủy đăng ký môn học thành công!', 'success')
    else:
        flash('Không tìm thấy thông tin đăng ký!', 'danger')
    return redirect(url_for('student.enrollments'))
