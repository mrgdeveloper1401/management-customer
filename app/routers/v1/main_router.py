from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import User, UserRole, Complaint, ComplaintStatus
from app.database import db

main_router = Blueprint('main', __name__)


@main_router.route('/')
def index():
    return render_template('index.html')

@main_router.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_customer:
        flash('شما دسترسی به این صفحه را ندارید', 'error')
        return redirect(url_for('main.index'))
    
    complaints = Complaint.query.filter_by(user_id=current_user.id)\
        .order_by(Complaint.created_at.desc()).all()
    
    return render_template('customer/dashboard.html', 
                          complaints=complaints)

@main_router.route('/complaints/create', methods=['GET', 'POST'])
@login_required
def create_complaint():
    if not current_user.is_customer:
        flash('فقط مشتریان می‌توانند شکایت ثبت کنند', 'error')
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        complaint_type = request.form.get('complaint_type')
        description = request.form.get('description')
        is_anonymous = request.form.get('is_anonymous') == 'on'

        if not complaint_type or not description:
            flash('لطفاً تمام فیلدهای ضروری را پر کنید', 'error')
            return redirect(url_for('main.create_complaint'))
    
        complaint = Complaint(
            user_id=current_user.id,
            complaint_type=complaint_type,
            description=description,
            is_anonymous=is_anonymous,
            status=ComplaintStatus.NEW
        )
        
        db.session.add(complaint)
        db.session.commit()
        
        flash(f'شکایت شما با موفقیت ثبت شد! کد رهگیری: {complaint.tracking_code}', 'success')
        return redirect(url_for('main.dashboard'))
    
    return render_template('complaints/create.html')

@main_router.route('/complaints/track', methods=['GET', 'POST'])
def track_complaint():
    if request.method == 'POST':
        tracking_code = request.form.get('tracking_code', '').strip()
        
        if not tracking_code:
            flash('لطفاً کد رهگیری را وارد کنید', 'error')
            return redirect(url_for('main.track_complaint'))
        
        complaint = Complaint.query.filter_by(tracking_code=tracking_code).first()
        
        if not complaint:
            flash('شکایتی با این کد رهگیری یافت نشد', 'error')
            return redirect(url_for('main.track_complaint'))
        
        return render_template('complaints/track_result.html', 
                              complaint=complaint)
    
    return render_template('complaints/track.html')

@main_router.route('/complaint-status')
def complaint_status():
    if current_user.is_authenticated:
        if current_user.is_superuser or current_user.is_staff:
            return redirect(url_for('main.admin_dashboard'))
        elif current_user.is_expert:
            return redirect(url_for('main.expert_dashboard'))
        else:
            return redirect(url_for('main.dashboard'))
    
    return redirect(url_for('main.track_complaint'))