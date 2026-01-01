# Customer Complaint Management System

این پروژه یک **سیستم مدیریت شکایات مشتریان / کارکنان** مبتنی بر **Flask + PostgreSQL** است که با معماری لایه‌ای (UI / Business Logic / Data Layer) طراحی شده و امکان ثبت، ارجاع، پاسخ‌دهی و گزارش‌گیری شکایات را فراهم می‌کند.

---

## 🚀 پیش‌نیازها (Requirements)

* **Python 3.12 یا بالاتر**
* PostgreSQL (در حال حاضر برای دیتابیس اصلی)
* pip

> ⚠️ پیشنهاد می‌شود پروژه را حتماً داخل محیط مجازی اجرا کنید.

---

## 🧱 ساختار کلی پروژه (خلاصه)

```
customer-complaint-system/
│
├── app/                # منطق اصلی برنامه (models, routes, services, ...)
├── static/             # فایل‌های static (css, js, images)
├── templates/          # قالب‌های HTML
├── tests/              # تست‌ها
├── main.py             # Entry Point برنامه
├── requirements.txt    # وابستگی‌ها
├── README.md
```

---

## ⚙️ راه‌اندازی پروژه روی لوکال

### 1️⃣ کلون پروژه

```bash
git clone git@github.com:mrgdeveloper1401/management-customer.git
cd customer-complaint-system
```

---

### 2️⃣ ایجاد و فعال‌سازی محیط مجازی

#### Linux / macOS

```bash
python3.12 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

---

### 4️⃣ تنظیم متغیرهای محیطی

یک فایل `.env` در ریشه پروژه بسازید:

```env
SECRET_KEY

FLASK_ENV
FLASK_HOST
FLASK_PORT

JWT_SECRET_KEY
JWT_ACCESS_TOKEN_EXPIRES
JWT_REFRESH_TOKEN_EXPIRES

POSTDB_NAME
POSTDB_HOST
POSTDB_PORT
POSTDB_USER
POSTDB_PASSWORD

MAIL_SERVER
MAIL_PORT
MAIL_USE_TLS
MAIL_USERNAME
MAIL_PASSWORD
MAIL_DEFAULT_SENDER

SMS_API_KEY=
SMS_API_URL=

```

> 📌 اطمینان حاصل کنید که دیتابیس PostgreSQL ساخته شده باشد.

---

### 5️⃣ اجرای مایگریشن‌ها (در صورت نیاز)

```bash
flask db upgrade
```

---

### 6️⃣ اجرای پروژه

```bash
python main.py
```

پس از اجرا، برنامه معمولاً روی آدرس زیر در دسترس خواهد بود:

```
http://127.0.0.1:5000 or http://127.0.0.1:8000
```

---

## 🧠 نکات معماری

* **PostgreSQL** برای داده‌های اصلی (Users, Complaints, Assignments, Responses)
* قابلیت توسعه برای استفاده از **MongoDB** جهت لاگ‌ها و Audit Trail
* استفاده از:

  * SQLAlchemy ORM
  * Flask-Migrate
  * معماری Service Layer

---

## 📌 وضعیت فعلی پروژه

* ✅ طراحی دیتابیس و مدل‌ها
* ✅ پشتیبانی از شکایت ناشناس
* ⏳ در حال توسعه: گزارش‌گیری، نقش‌ها، UI کامل

