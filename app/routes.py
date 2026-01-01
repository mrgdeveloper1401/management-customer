from flask import Blueprint, request, jsonify, g, current_app
from app.utils import token_required
from app.database import DatabaseManager

# ---------- AUTH (نمونه ساده) ----------
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def fake_login():
    """
    لاگین تستی:
    فقط برای پروژه دانشگاهی
    """
    g.user_id = 1
    return jsonify({
        "success": True,
        "message": "login fake success",
        "token": "fake-token"
    })


# ---------- COMPLAINT ----------
complaint_bp = Blueprint("complaint", __name__, url_prefix="/complaints")


@complaint_bp.route("/create", methods=["POST"])
@token_required
def create_complaint():
    data = request.get_json()

    if not data or "title" not in data or "description" not in data:
        return jsonify({
            "success": False,
            "error": "title و description الزامی هستند"
        }), 400

    is_anonymous = int(data.get("is_anonymous", False))

    db: DatabaseManager = current_app.db_manager

    db.execute_query(
        """
        INSERT INTO complaints (user_id, title, description, is_anonymous)
        VALUES (?, ?, ?, ?)
        """,
        (
            g.user_id,              # هویت واقعی ذخیره می‌شود
            data["title"],
            data["description"],
            is_anonymous
        )
    )

    return jsonify({
        "success": True,
        "message": "شکایت با موفقیت ثبت شد",
        "anonymous": bool(is_anonymous)
    }), 201


@complaint_bp.route("/list", methods=["GET"])
@token_required
def list_complaints():
    db: DatabaseManager = current_app.db_manager

    complaints = db.execute_query(
        """
        SELECT c.complaint_id, c.title, c.description, c.is_anonymous,
               u.full_name
        FROM complaints c
        JOIN users u ON c.user_id = u.user_id
        """,
        fetch_all=True
    )

    result = []
    for c in complaints:
        result.append({
            "complaint_id": c["complaint_id"],
            "title": c["title"],
            "description": c["description"],
            "complainant": "ناشناس" if c["is_anonymous"] else c["full_name"]
        })

    return jsonify({
        "success": True,
        "complaints": result
    })


# ---------- REGISTER BLUEPRINTS ----------
def init_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(complaint_bp)

def main_router():
    pass
