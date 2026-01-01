# app/exceptions.py
class ComplaintManagementError(Exception):
    """خطای پایه سیستم مدیریت شکایات"""
    pass


class ValidationError(ComplaintManagementError):
    """خطای اعتبارسنجی داده‌ها"""
    def __init__(self, message: str = "اعتبارسنجی ناموفق"):
        super().__init__(message)


class AuthenticationError(ComplaintManagementError):
    """خطای احراز هویت"""
    def __init__(self, message: str = "احراز هویت ناموفق"):
        super().__init__(message)


class AuthorizationError(ComplaintManagementError):
    """خطای مجوزدهی"""
    def __init__(self, message: str = "دسترسی غیرمجاز"):
        super().__init__(message)


class PermissionDeniedError(AuthorizationError):
    """خطای عدم دسترسی"""
    def __init__(self, message: str = "شما مجوز انجام این عملیات را ندارید"):
        super().__init__(message)


class ResourceNotFoundError(ComplaintManagementError):
    """خطای عدم یافتن منبع"""
    def __init__(self, resource_type: str = "منبع", resource_id: str = ""):
        message = f"{resource_type} یافت نشد"
        if resource_id:
            message += f": {resource_id}"
        super().__init__(message)


class ComplaintNotFoundError(ResourceNotFoundError):
    """خطای عدم یافتن شکایت"""
    def __init__(self, complaint_id: str = ""):
        super().__init__("شکایت", complaint_id)


class UserNotFoundError(ResourceNotFoundError):
    """خطای عدم یافتن کاربر"""
    def __init__(self, user_id: str = ""):
        super().__init__("کاربر", user_id)


class DatabaseError(ComplaintManagementError):
    """خطای پایگاه داده"""
    def __init__(self, message: str = "خطای پایگاه داده"):
        super
