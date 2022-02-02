> 장고의 특징 중 하나는 ORM QuerySet을 적극적으로 사용하는 것이다. 
<br>하지만 앱 규모가 커질수록 QuerySet 중복코드가 늘어나면서 유지관리가 어려워지는 단점이 있다. 
<br>이 문제를 해결하기 위한 방법 중 하나가 `Manager` 을 사용하는 것이다. 

<br>

### Manager

- 장고는 DB 오브젝트를 검색하기 위해 모델 클래스의 Manager 를 통해 QuerySet 을 구성한다. 

- 장고는 모든 모델에 objects 라는 이름의 디폴트 매니저를 추가한다. 그렇기에 별도의 Manager 추가 없이 QuerySet 을 사용할 수 있다. 

- `QuerySet` 은 SQL 구문의 SELECT 와 매치되고, `filter` 는 WHERE, LIMIT 가 유사하다.

<br>

### Custom manager 사용 

- Manager의 메서드 추가

  - 모델에 "테이블 수준" 기능을 추가할 수 있다. 
  - "Row-level" 기능을 작성할 땐 Model 메소드를 사용하는 것이 좋다. 

  ```python
  from django.db import models
  from django.db.models.function import Coalesce
  
  class PollManager(models.Manager):
    def with_counts(self):
      return self.annotate(num_responses=Coalesce(models.Count("response"), 0))
  
  class OpinionPoll(models.Model):
    question = models.CharField(max_lentgh=200)
    objects = PollManager()
    
  class Response(models.Model):
    poll = models.ForeignKey(OpinionPoll, on_delete=models.CASCADE)
  
  ```

  `num_responses`라는 추가 속성을 가진 objects 의 QuerySet 을 얻기 위해  `OpinionPoll.objects.with_counts()` 를 사용할 수 있다. 

<br>

- 매니저가 리턴하는 초기 QuerySet 수정

  - `Manager.get_queryset()` 을 오버라이딩 한다.
  - 기본 QuerySet 은 해당 모델의 모든 데이터를 리턴하도록 작성되어 있다. 
  - `filter()` `exclude()` 등 모든 쿼리셋 메서드를 사용할 수 있다.  

  ```python
  class AuthorManager(models.Manager):
    def get_queryset(self):  # 반드시 QuerySet을 반환해야 한다.
      return super().get_queryset().filter(role='A') 
  
  class EditorManager(models.Manager):
    def get_queryset(self):
      return super().get_queryset().filter(role='E')
  
  class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=[('A', _('Author')), ('E', _('Editor'))])
    
    people = models.Manager()  # default manager
    authors = AuthorManager()  # custom
    editors = EditorManager()  # custom
  ```

<br>

### Default manager 역할과 선정방식

- Manager를 재정의할 경우 해당 모델의 Manager name 순서가 중요하다.

- 첫번째 정의되는 Manager 가 `default manager` 가 된다.
- dumpdata 기능 또는 써드파티 앱에서는 재정의 여부를 알 수 없다. 
  - 그러므로 `Model._default_manager` 를 사용해 접근한다. 
  - `User._default_manager.all()` 
  - 주의) dumpdata 는 모든 데이터를 백업하는 용도로 사용하지만 default manager 을 커스텀한 경우 필터링된 데이터를 백업하는 결과로 이어질 수 있다. 

<br>

### QuerySet 메서드로 Manager 생성

- ORM 중복코드를 제거하려 Manager 를 사용하지만, 그 안에서 또 QuerySet 중복코드가 발생할 수 있다.

- `QuerySet.as_manager()` 를 사용한다. 

  - 장고의 설계 철학 중 DRY(Don't Repeat Yourself) 따른다.

  ```python
  class PersonQuerySet(models.QuerySet):
    def authors(self):
      return self.filter(role='A')
    
    def editors(self):
      return self.filter(role='E')
  
  class Person(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=[('A', _('Author')), ('E', _('Editor'))])
    people = PersonQuerySet.as_manager() 
  ```

- 사용 시 주의할 점 (몇가지 규칙) 

```python
class CustomQuerySet(models.QuerySet):
  # 퍼블릭 메서드 : Manager, QuerySet 모두 가능 
  def public_method(self):
    return
  
  # 프라이빗 메서드 : QuerySet 만 가능 
  def _private_method(self):
    return
  
  # queryset_only 옵션 True : QuerySet 만 가능 
  def opted_out_public_method(self):
    return opted_out_public_method.queryset_only = True
  
  # queryset_only 옵션 False : Manager, QuerySet 모두 가능 
  def _opted_in_private_method(self):
    return _opted_in_private_method.queryset_only = False 
```

<br>

### Manager 와 QuerySet 모두 커스텀

- `Manager.from_queryset()` 를 사용한다. 

```python
class CustomManager(models.Manager):
  def manager_only_method(self):
    return
  
class CustomQuerySet(models.QuerySet):
  def manager_and_queryset_method(self):
    return

class MyModel(models.Model):
  objects = CustomManager.from_queryset(CustomQuerySet())
```

<br>

### DRY 적용 사례

- active 필도를 가지고 있는 3개의 모델이 있다.

```python
class Post(models.Model):
  active = models.BooleanField(default=True)

class Comment(models.Model):
  active = models.BooleanField(default=True)
  
class Reply(models.Model):
  active = models.BooleanField(default=True)
```

- active 필드를 필터링하기 위한 QuerySet 중복코드를 해결하기 위해 커스텀 Manager 을 작성한다.

```python
class ActiveManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(active=True)
  
class Post(models.Model):
  objects = models.Manager()  # default manager
  active_objects = ActiveManager()

class Comment(models.Model):
  objects = models.Manager()  # default manager
  active_objects = ActiveManager()

class Reply(models.Model):
  objects = models.Manager()  # default manager
  active_objects = ActiveManager()
```

- Manager 정의 중복코드를 상속을 활용해 제거한다. 

```python
class ActiveManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(active=True)
  
class AbstractBase(models.Model):
  objects = models.Manager()
  active_objects = ActiveManager()
  
  class Meta:
    abstract = True 
  
class Post(AbstractBase):
  pass

class Comment(AbstractBase):
  pass

class Reply(AbstractBase):
  pass
```

- 새로운 Manager 가 추가되면 default manager가 변경되는 이슈가 발생한다.

```python
class ActiveManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(active=True)
  
class AbstractBase(models.Model):
  objects = models.Manager()
  active_objects = ActiveManager()
  
  class Meta:
    abstract = True
    default_manager_name = 'objects'  # default manager 를 명시한다. 

class NonActiveManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(active=False)

class Reply(AbstractBase):
  non_active_objects = NonActiveManager()  # 상위클래스에서 명시되었으므로, default manager가 아니다. 하지만 Reply 내부에서 default_manager_name 을 지정하면 변경될 수 있다. 
```

<br>

### 참고

- https://docs.djangoproject.com/en/4.0/topics/db/managers/ 
- http://blog.hwahae.co.kr/all/tech/tech-tech/4108/ 

