# Session 23 - Learning Resource Management API

## 1. Cấu trúc project

```text
learning_resource_api/
├── main.py
├── middleware.py
├── security.py
├── auth.py
├── requirements.txt
├── README.md
├── REPORT.md
├── TEST_CASES.md
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── resource.py
│
├── schemas/
│   ├── __init__.py
│   ├── auth.py
│   ├── user.py
│   └── resource.py
│
├── services/
│   ├── __init__.py
│   ├── auth.py
│   └── resource.py
│
└── routers/
    ├── __init__.py
    ├── auth.py
    ├── users.py
    └── resources.py
```

## 2. Cài đặt

```bash
python -m venv .venv
```

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Nếu PowerShell báo ExecutionPolicy:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Cài thư viện:

```bash
pip install -r requirements.txt
```

## 3. Chạy

Đứng tại thư mục có `main.py`:

```bash
uvicorn main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## 4. Tài khoản

```text
admin01 / 123456 / admin / active
student01 / 123456 / user / active
student02 / 123456 / user / inactive
```

## 5. Luồng code

```text
Router
  ↓
Dependency Authentication
  ↓
Dependency Authorization
  ↓
Service
  ↓
Model/Data
```

JWT được tạo trong `security.py`.

JWT được xác thực trong `auth.py`.

Nghiệp vụ tài nguyên nằm trong `services/resource.py`.

API nằm trong `routers/`.

Middleware và CORS được đăng ký trong `main.py`.

## 6. API

- POST `/auth/login`
- GET `/users/me`
- GET `/resources`
- GET `/resources/{resource_id}`
- POST `/resources`
- PATCH `/resources/{resource_id}/publish`
- DELETE `/resources/{resource_id}`
- GET `/health`

## 7. Test Swagger

Đăng nhập:

```json
{
  "username": "admin01",
  "password": "123456"
}
```

Copy `access_token`.

Swagger → Authorize → nhập:

```text
Bearer <access_token>
```

Sau đó test các API Admin.

Với `student01`, User chỉ xem được tài nguyên đã publish.

