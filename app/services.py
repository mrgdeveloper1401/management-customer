# # app/services.py
# import logging
# from datetime import datetime
# from typing import Optional, Dict, Any, List
#
# from werkzeug.security import generate_password_hash, check_password_hash
#
# from app.models import User, UserRole
# from app.exceptions import ValidationError, UserNotFoundError
#
# logger = logging.getLogger(__name__)
#
#
# class UserService:
#     """سرویس مدیریت کاربران"""
#
#     def __init__(self):
#         # فرض بر اینکه این سرویس با یک DB واقعی کار می‌کند
#         self.users_db: Dict[int, User] = {}  # نمونه DB موقت
#
#     def create_user(self, user_data: Dict[str, Any]) -> User:
#         """ایجاد کاربر جدید"""
#         if 'username' not in user_data or 'email' not in user_data or 'password' not in user_data:
#             raise ValidationError("username, email و password الزامی هستند")
#
#         # بررسی تکراری بودن کاربر
#         for u in self.users_db.values():
#             if u.username == user_data['username'] or u.email == user_data['email']:
#                 raise ValidationError("نام کاربری یا ایمیل تکراری است")
#
#         user = User(
#             user_id=len(self.users_db) + 1,
#             username=user_data['username'],
#             email=user_data['email'],
#             full_name=user_data.get('full_name', ''),
#             phone=user_data.get('phone'),
#             address=user_data.get('address'),
#             role=user_data.get('role', UserRole.CUSTOMER.value),
#             is_active=True,
#             created_at=datetime.now(),
#             updated_at=datetime.now()
#         )
#         user.set_password(user_data['password'])
#         self.users_db[user.user_id] = user
#         logger.info(f"کاربر ایجاد شد: {user.username}")
#         return user
#
#     def get_user(self, user_id: int) -> User:
#         """دریافت کاربر با ID"""
#         user = self.users_db.get(user_id)
#         if not user:
#             raise UserNotFoundError(str(user_id))
#         return user
#
#
# class AuthService:
#     """سرویس احراز هویت و مدیریت رمز عبور"""
#
#     def __init__(self):
#         # برای نمونه یک DB موقت
#         self.user_service = UserService()
#
#     def change_password(self, user_id: int, current_password: str, new_password: str) -> bool:
#         """
#         تغییر رمز عبور کاربر
#         برمی‌گرداند True اگر موفق بود، False اگر رمز فعلی اشتباه بود
#         """
#         try:
#             user = self.user_service.get_user(user_id)
#         except UserNotFoundError:
#             return False
#
#         if not check_password_hash(user.password_hash, current_password):
#             return False
#
#         user.set_password(new_password)
#         user.updated_at = datetime.now()
#         logger.info(f"رمز عبور کاربر {user.username} تغییر یافت")
#         return True
#
#
# # ایجاد یک instance آماده برای استفاده در routes
# auth_service = AuthService()
# user_service = auth_service.user_service  # اگر نیاز به دسترسی به UserService دارید
