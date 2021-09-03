> Framework

- 클래스와 라이브러리 모임
- 재사용할 수 있는 수많은 코드를 프레임워크로 통일



> Web Framework

- 주 목적 : 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것
- 데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등



> Framework Architecture

- MVC Design Pattern (model-view-controller)
- Django는 `MTV` 패턴이라고 함



> MTV Pattern

- Model
  - 데이터베이스의 기록을 관리(추가, 수정, 삭제)
- Template
  - MVC에서 view 와 유사함
  - 실제 내용을 보여주는 데 사용
- View
  - MVC에서 controller 와 유사함
  - HTTP 요청 수신, 응답 반환
  - Model을 통해 요청을 충족시키는 데 필요한 데이터 접근
  - Template 에게 응답의 서식 설정을 맡김



> 프로젝트 생성 및 구조

```bash
$ django-admin startproject config .
```

config : 설정폴더(프로젝트 폴더)

​	__init__.py : 모듈이라는 것을 명시 (장고는 필수)

​	asgi.py : 비동기 서버 게이트웨이 인터페이스, 배포시 활용

​	settings.py : 모든 설정을 포함

​	urls.py : 사이트의 url과 적절한 views의 연결 지정

​	wsgi.py : 웹서버와 연결 및 소통하는 것을 도움, 배포시 활용

​	manage.py : 장고 프로젝트와 다양한 방법으로 상호작용하는 CLI 유틸리티



> Application 생성 및 구조

- 네임은 복수형으로 하는 것을 권장

```bash
$ python manage.py startapp <app_name>
```

migrations/

__init__.py

admin.py : 관리자용 페이지 설정

apps.py : 앱의 정보 작성

models.py : Model 정의

tests.py : 프로젝트의 테스트코드 작성

views.py : View 정의

<br>

---

### URL



> Variable Routing

- path에 값을 보내는 방법
  - 예) `[default URI]/<user_id>/<note_id>`
- query string 과는 방식이 다르다.

