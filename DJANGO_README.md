# Django Hello World

Một ứng dụng Django đơn giản hiển thị "Hello World!".

## Cấu trúc dự án

```
src/
  ├── manage.py                 # Django management script
  ├── helloworld/               # Django project folder
  │   ├── __init__.py
  │   ├── settings.py           # Cấu hình Django
  │   ├── urls.py               # URL routing
  │   └── wsgi.py               # WSGI application
  └── app/                       # Django app
      ├── __init__.py
      ├── apps.py               # App configuration
      └── views.py              # View functions
```

## Chạy ứng dụng

```bash
cd src
python manage.py runserver
```

Sau đó truy cập: `http://localhost:8000/`

## Thêm một view mới

Edit file [src/app/views.py](src/app/views.py) và thêm function view mới, rồi cập nhật URLs trong [src/helloworld/urls.py](src/helloworld/urls.py).
