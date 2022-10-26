# SocialNetwork
## cách cài đặt poetry
### tải poetry về bằng cách mở Powershell và chạy ' (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - '

### sau đo mở 'edit system environment variables' chọn 'environment variables', rồi thêm vào Path cái đường dẫn của nó (khi chạy lệnh ở trên nó có hướng dẫn thêm cái gì vào Path)
## sử dụng poetry
### 'poetry install' để cài đặt tất cả những thứ có trong file pyproject.toml, nếu muốn thay đổi version chỉ cẩn chỉnh sửa file này rồi chạy 'poetry install'
(chạy lệnh này trong thư mục chứa project)
### để thêm các package cần thiết vào trong project chạy lệnh 'poetry add tên package' trong thư mục chứa project
