from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from app.database import db
from app.models import User, UserRole


auth_router = Blueprint("auth", __name__)

@auth_router.route("/login", methods=['GET', "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # get user
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user, remember=True)
            flash('با موفقیت وارد شدید!', 'success')
            return redirect(url_for("main.dashboard"))
        else:
            flash('نام کاربری یا رمز عبور اشتباه است', 'error')
    
    return render_template('auth/login.html')

# logout route
@auth_router.route("/logout")
@login_required
def logout():
    logout_user()
    flash('با موفقیت خارج شدید', 'info')
    return redirect(url_for('main.index'))

# register user
@auth_router.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
        
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password', '')
        full_name = request.form.get('full_name')
        phone = request.form.get('phone')
        
        # validate
        if password != confirm_password:
            flash('رمز عبور و تأیید رمز عبور مطابقت ندارند', 'error')
            return redirect(url_for('auth.register'))
        
        # check user exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('این نام کاربری قبلاً ثبت شده است', 'error')
            return redirect(url_for('auth.register'))
        
        # check email exists
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('این ایمیل قبلاً ثبت شده است', 'error')
            return redirect(url_for('auth.register'))
        
        existing_email = User.query.filter_by(phone=phone).first()
        if existing_email:
            flash("این شماره موبایل قبلا ثبت شده هست", 'error')
            return redirect(url_for('auth.register'))

        # create new user
        new_user = User(
            username=username,
            email=email,
            full_name=full_name,
            phone=phone,
            password_hash=generate_password_hash(password),
            role=UserRole.CUSTOMER
        )
        
        # commit to database
        db.session.add(new_user)
        db.session.commit()
        
        flash('ثبت‌نام با موفقیت انجام شد! لطفاً وارد شوید', 'success')
        return redirect(url_for("main.dashboard"))
    
    return render_template("auth/register.html")