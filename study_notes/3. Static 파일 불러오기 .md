# Static 파일 불러오기

---

- static 폴더 : img, css, js 파일을 저장하는 폴더

1. settings.py에 static 폴더 지정

```python
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
```

2. html에서 static 폴더에 있는 파일불러오기

```html
<!DOCTYPE html>
<!-- 꼭 선언해주기 -->
{% lode static %}   
```

 → 이제 html 파일에서 static 폴더안에 접근할 수 있는 권한을 가지게 됨.

- 불러오기 형식 : {% static 'static 하위경로' %}

```html
<!-- css 불러오기 -->
<link rel="stylesheet" href="{% static "main.css" %}">

<!-- image 불러오기 -->
<img src="{% static "images/my_photo.JPG" %}" alt="사람사진">
```