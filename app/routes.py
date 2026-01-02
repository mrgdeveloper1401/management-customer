from flask import Blueprint, render_template, request, redirect, url_for

main_router = Blueprint('main', __name__)

# main router
@main_router.route('/')
def index():
    return render_template('index.html')

# @main_router.route('/complaints/create')
# def create_complaint():
#     return render_template('complaints/create.html')

# @main_router.route('/complaints/track')
# def track_complaint():
#     return render_template('customer/track_complaint.html')

# @main_router.route('/admin/dashboard')
# def admin_dashboard():
#     return render_template('admin/dashboard.html')
