# TEST CASES

| STT | Nội dung | Kết quả mong đợi |
|---|---|---|
| 1 | GET /health | 200 |
| 2 | Login admin đúng | 200 + JWT |
| 3 | Login username sai | 401 |
| 4 | Login password sai | 401 |
| 5 | Login student02 bị khóa | 403 |
| 6 | GET /users/me không token | 401 |
| 7 | GET /users/me token đúng | 200 |
| 8 | JWT sai chữ ký | 401 |
| 9 | JWT hết hạn | 401 |
| 10 | JWT thiếu sub | 401 |
| 11 | User GET /resources | Chỉ resource published |
| 12 | Admin GET /resources | Tất cả resource |
| 13 | User GET resource unpublished | 404 |
| 14 | Admin GET resource unpublished | 200 |
| 15 | User POST /resources | 403 |
| 16 | Admin POST /resources | 201 |
| 17 | User PATCH publish | 403 |
| 18 | Admin PATCH publish | 200 |
| 19 | User DELETE | 403 |
| 20 | Admin DELETE | 204 |
| 21 | Resource không tồn tại | 404 |
| 22 | Khóa user sau khi cấp token | Token cũ → 403 |
| 23 | Token role giả super_admin | Vẫn bị 403 nếu user thật là user |
| 24 | OPTIONS request | CORS preflight hoạt động |
| 25 | Origin localhost:3000 | Được phép |
| 26 | Origin localhost:5173 | Được phép |
| 27 | Origin website khác | Không được cấp CORS |
| 28 | Kiểm tra X-Request-ID | Có header |
| 29 | Kiểm tra X-Process-Time | Có header |
