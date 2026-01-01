# # app/validators.py
# from typing import Dict, Any, List, Optional
# from datetime import datetime
# import re
# from app.exceptions import ValidationError
#
#
# class BaseValidator:
#     """کلاس پایه برای اعتبارسنجی"""
#
#     @staticmethod
#     def validate_required(value, field_name: str):
#         if value is None or (isinstance(value, str) and not value.strip()):
#             raise ValidationError(f"فیلد '{field_name}' الزامی است")
#
#     @staticmethod
#     def validate_string(value, field_name: str, min_length: int = None,
#                         max_length: int = None, pattern: str = None):
#         if value is not None:
#             if not isinstance(value, str):
#                 raise ValidationError(f"فیلد '{field_name}' باید رشته باشد")
#             value = value.strip()
#             if min_length and len(value) < min_length:
#                 raise ValidationError(f"فیلد '{field_name}' باید حداقل {min_length} کاراکتر باشد")
#             if max_length and len(value) > max_length:
#                 raise ValidationError(f"فیلد '{field_name}' حداکثر باید {max_length} کاراکتر باشد")
#             if pattern and not re.match(pattern, value):
#                 raise ValidationError(f"فیلد '{field_name}' قالب نامعتبر دارد")
#
#     @staticmethod
#     def validate_email(value: str, field_name: str = "ایمیل"):
#         if value:
#             email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#             if not re.match(email_pattern, value):
#                 raise ValidationError(f"فرمت {field_name} نامعتبر است")
#
#     @staticmethod
#     def validate_phone(value: str, field_name: str = "تلفن"):
#         if value:
#             phone_pattern = r'^(\+98|0)?9\d{9}$'
#             if not re.match(phone_pattern, value.replace(' ', '')):
#                 raise ValidationError(f"فرمت {field_name} نامعتبر است")
#
#     @staticmethod
#     def validate_number(value, field_name: str, min_value: float = None, max_value: float = None):
#         pass
