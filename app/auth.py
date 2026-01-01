# app/auth.py
import jwt
import logging
from datetime import datetime, timedelta
from functools import wraps
from typing import Optional, Dict, Any, List
from flask import request, jsonify, g

from app.config import Config
from app.exceptions import AuthenticationError, PermissionDeniedError
from app.database import DatabaseManager
from app.services import UserService

logger = logging.getLogger(__name__)


class AuthService:
    """سرویس احراز هویت و مدیریت جلسات"""

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def create_access_token(self, user_data: Dict[str, Any]) -> str:
        """ایجاد توکن دسترسی"""
        payload = {
            'user_id': user_data['user_id'],
            'username': user_data['username'],
            'email': user_data['email'],
            'role': user_data['role'],
            'full_name': user_data['full_name'],
            'exp': datetime.now() + timedelta(minutes=Config.JWT_ACCESS_TOKEN_EXPIRES),
            'iat': datetime.now(),
            'type': 'access'
        }
        return jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')

    def create_refresh_token(self, user_id: int) -> str:
        """ایجاد توکن بازنشانی"""
        payload = {
            'user_id': user_id,
            'exp': datetime.now() + timedelta(minutes=Config.JWT_REFRESH_TOKEN_EXPIRES),
            'iat': datetime.now(),
            'type': 'refresh'
        }
