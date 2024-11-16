from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from app import db, bcrypt  # Import bcrypt từ app
from app.models import User

bp = Blueprint('auth', __name__)

# Đăng ký


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(
            password).decode('utf-8')  # Mã hóa mật khẩu với bcrypt

        if User.query.filter_by(username=username).first():
            flash('Tên đăng nhập đã tồn tại!', 'danger')
        else:
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Đăng ký thành công!', 'success')
            return redirect(url_for('auth.login'))

    return render_template('register.html')

# Đăng nhập


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        # Kiểm tra mật khẩu với bcrypt
        if user and bcrypt.check_password_hash(user.password, password):
            session['logged_in'] = True
            session['username'] = user.username
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('student.index'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không đúng!', 'danger')

    return render_template('login.html')

# Đăng xuất


@bp.route('/logout')
def logout():
    session.clear()
    flash('Đã đăng xuất!', 'success')
    return redirect(url_for('auth.login'))
