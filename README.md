# SocialNetwork
## cách cài đặt poetry
### tải poetry về bằng cách mở Powershell và chạy ' (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - '

### sau đo mở 'edit system environment variables' chọn 'environment variables', rồi thêm vào Path cái đường dẫn của nó (khi chạy lệnh ở trên nó có hướng dẫn thêm cái gì vào Path)
## sử dụng poetry
### đối với project mới, ta chạy lệnh 'poetry init' để tạo file pyproject.toml chứa các package cần cài đặt trong project (file này ta có thể chỉnh sửa version của từng package rồi sau đó chạy lẹnh 'poetry install' để lưu thay đổi)

### để thêm các package cần thiết vào trong project chạy lệnh 'poetry add tên package' trong thư mục chứa project

### lệnh 'poetry install' để cài đặt tất cả những package có trong file pyproject.toml,

### bật môi trường ảo ta chạy lệnh 'poetry shell' (để sử dụng poetry cho project tất nhiên bắt buộc phải bật môi trường ảo)
### để tắt môi trường ảo chạy lệnh 'exit'
### để thêm các package cần thiết vào trong project chạy lệnh 'poetry add tên package'
### note : môi trường ảo trong poetry không cần đặt tên như anaconda, poetry sẽ tự đặt cho project đấy
### để biết thêm chi tiết tham khảo ở : https://python-poetry.org/docs/basic-usage/

### ngoài ra để gỡ cài đặt poetry ra khỏi máy thì ta mở Powershell và chạy 
### '(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - --uninstall'
