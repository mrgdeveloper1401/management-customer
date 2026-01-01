import os
import uuid
import logging
import hashlib
from functools import wraps
from typing import Optional, List

from flask import request, jsonify
from werkzeug.utils import secure_filename
from jinja2 import Template

logger = logging.getLogger(__name__)


# ----------------- بررسی فایل -----------------

def allowed_file(filename: str, allowed_extensions: Optional[List[str]] = None) -> bool:
    from app.config import Config
    if allowed_extensions is None:
        allowed_extensions = list(Config.ALLOWED_EXTENSIONS.keys())
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


# ----------------- ذخیره فایل -----------------

def save_uploaded_file(file, subdirectory: str = '') -> str:
    from app.config import Config

    upload_dir = os.path.join(Config.UPLOAD_FOLDER, subdirectory)
    os.makedirs(upload_dir, exist_ok=True)

    original_filename = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4().hex}_{original_filename}"
    file_path = os.path.join(upload_dir, unique_filename)

    file.save(file_path)
    logger.info(f"File saved: {file_path}")
    return file_path


# ----------------- هش -----------------

def hash_string(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


# ----------------- Token Required -----------------

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({
                "success": False,
                "error": "Token is missing"
            }), 401

        # اینجا بعداً می‌تونی JWT واقعی اضافه کنی
        return f(*args, **kwargs)
    return decorated


# ----------------- PDF (اختیاری) -----------------

def render_pdf_from_template(template_str: str, context: dict, output_path: str) -> str:
    import pdfkit  # import داخل تابع (بهتر و امن‌تر)

    template = Template(template_str)
    html_content = template.render(**context)

    pdfkit.from_string(html_content, output_path)
    return output_path


# ----------------- Error Formatter (مهم) -----------------

def format_error_response(error):
    """ساخت پاسخ استاندارد خطا"""
    return {
        "success": False,
        "error": str(error),
        "error_type": error.__class__.__name__
    }
