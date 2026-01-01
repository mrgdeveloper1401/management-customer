import uuid

from app.database import db
from enum import Enum


class UserRole(Enum):
    CUSTOMER = "customer"
    EXPERT = "expert"
    ADMIN = "admin"

class ComplaintStatus(Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    ANSWERED = "answered"
    CLOSED = "closed"


class TimestampMixin:
    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime,
        onupdate=db.func.now(),
    )


class SoftDeleteMixin:
    is_deleted = db.Column(db.Boolean, default=False)


class User(TimestampMixin, SoftDeleteMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    email = db.Column(db.String(100), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    role = db.Column(
        db.Enum(UserRole),
        nullable=False
    )


class Complaint(TimestampMixin, SoftDeleteMixin, db.Model):
    __tablename__ = "complaints"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )
    tracking_code = db.Column(
        db.String(20),
        unique=True,
        nullable=False,
        default=lambda: uuid.uuid4().hex[:10].upper()
    )
    invoice_number = db.Column(db.String(50), nullable=True)
    complaint_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(
        db.Enum(ComplaintStatus),
        default=ComplaintStatus.NEW,
        nullable=False
    )
    is_anonymous = db.Column(db.Boolean, default=True)


class Attachment(TimestampMixin, SoftDeleteMixin, db.Model):
    __tablename__ = "attachments"
    id = db.Column(db.Integer, primary_key=True)
    complaint_id = db.Column(
        db.Integer,
        db.ForeignKey("complaints.id"),
        nullable=False
    )
    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_type = db.Column(db.String(50), nullable=False)


class Assignment(TimestampMixin, SoftDeleteMixin, db.Model):
    __tablename__ = "assignments"

    id = db.Column(db.Integer, primary_key=True)
    complaint_id = db.Column(
        db.Integer,
        db.ForeignKey("complaints.id"),
        nullable=False
    )
    expert_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )
    assigned_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )
    assigned_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )
    notes = db.Column(db.Text, nullable=True)


class Response(TimestampMixin, SoftDeleteMixin, db.Model):
    __tablename__ = "responses"

    id = db.Column(db.Integer, primary_key=True)
    complaint_id = db.Column(
        db.Integer,
        db.ForeignKey("complaints.id"),
        nullable=False
    )
    responded_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )
    response_text = db.Column(db.Text, nullable=False)
    is_final = db.Column(db.Boolean, default=False)
    responded_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )


class Message(TimestampMixin, SoftDeleteMixin, db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )
    receiver_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )
    complaint_id = db.Column(
        db.Integer,
        db.ForeignKey("complaints.id"),
        nullable=True
    )
    content = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
