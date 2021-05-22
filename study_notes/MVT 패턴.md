# MVT 패턴

---

### Overview

- python -m venv [가상환경명] : 가상환경 만들기
- source [가상환경명]/bin/activate : 가상환경 실행시키기 (macOS)
- pip install django : 장고 다운로드
- django-admin startproject [프로젝트 이름] : 다운받은 장고로 프로젝트 만들기
- python [manage.py](http://manage.py) runserver : 만든 프로젝트 안에서 터미널을 기동하여 서버 작동시키기

---

# MTV ?

- Model, Template, View

### Template

- 사용자가 보이는 영역
- HTML
- CSS
- 템플릿 언어

### Model

- DataBase (DB)

### View

- 데이터를 처리하는 곳
- MTV 중에서 핵심