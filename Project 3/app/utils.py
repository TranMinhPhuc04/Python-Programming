from functools import wraps
from flask import redirect, url_for, session, flash


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash('Bạn cần đăng nhập để truy cập chức năng này.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function
