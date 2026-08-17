# REPORT - PHÂN TÍCH VÀ THIẾT KẾ

## A1. Input / Output

| API | Input | Output | Lỗi |
|---|---|---|---|
| POST /auth/login | username, password | JWT | 401, 403 |
| GET /users/me | Bearer JWT | Current user | 401, 403 |
| GET /resources | Bearer JWT | List resource | 401 |
| GET /resources/{id} | id + JWT | Resource | 401, 404 |
| POST /resources | ResourceCreate + JWT | Resource | 401, 403, 422 |
| PATCH /resources/{id}/publish | id + JWT | Resource | 401, 403, 404 |
| DELETE /resources/{id} | id + JWT | 204 | 401, 403, 404 |
| GET /health | Không | Health | - |

## A2. Giải pháp

### JWT

Payload:

```json
{
  "sub": "admin01",
  "role": "admin",
  "exp": 1780000000
}
```

Dùng HS256 để ký token.

### Current User

`get_current_user()`:

1. Decode JWT.
2. Verify chữ ký.
3. Kiểm tra `exp`.
4. Lấy `sub`.
5. Tìm user thật trong `models/user.py`.
6. Kiểm tra `is_active`.
7. Trả current user.

Role trong JWT không được dùng trực tiếp để cấp quyền.

### Authorization

`require_admin()` gọi `get_current_user()` trước, sau đó lấy role từ user thật.

### Middleware

Mỗi request:

```text
Request
↓
UUID request_id
↓
Start timer
↓
call_next()
↓
Response
↓
X-Request-ID
X-Process-Time
↓
Log
```

Middleware không tự trả 401.

### CORS

Chỉ cho phép:

```text
http://localhost:3000
http://localhost:5173
```

Cho phép Authorization, Content-Type và các method cần thiết.

### Status code

```text
401 = chưa xác thực / JWT không hợp lệ
403 = đã xác thực nhưng không có quyền / tài khoản khóa
404 = resource không tồn tại hoặc unpublished đối với User
```

## A3. Luồng

### Login

```text
Login
↓
Tìm user
↓
Sai username → 401
↓
Inactive → 403
↓
Sai password → 401
↓
Tạo JWT
↓
Response
```

### Current User

```text
Bearer JWT
↓
Verify JWT
↓
Check exp
↓
Get sub
↓
Find user thật
↓
Check is_active
↓
Current User
```

### Admin

```text
get_current_user()
↓
role thật == admin?
↓
Có → cho phép
Không → 403
```

### CORS Preflight

```text
OPTIONS
↓
CORSMiddleware
↓
Check Origin
↓
Trả CORS headers
```

## B. Năm bẫy

1. Token hợp lệ nhưng tài khoản bị khóa → `403`.
2. Token role `super_admin` giả → role thật từ hệ thống, không được cấp Admin.
3. Token hết hạn → `401`.
4. OPTIONS không JWT → CORS xử lý, không tự trả `401`.
5. User xem resource unpublished → `404`.
