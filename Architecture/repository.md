### 저장소 패턴?

- 데이터가 있는 저장소를 추상화하여 중앙집중처리 방식을 구성하고, 데이터 접근과 구현사항을 감춘다.
- 모든 데이터가 메모리상에 존재하는 것처럼 가정한다.
- 저장소를 제외한 다른 레이어는 더이상 저장소의 구현에 대해 신경 쓸 필요 없이 인터페이스로만 소통한다.
- 고수준 모듈인 비즈니스 로직(도메인 모델)은 DB계층에 의존하면 안된다. (DIP) 

<img width="400" alt="image" src="https://user-images.githubusercontent.com/42771578/222875322-6de36dfe-dd1b-44ad-8479-e6cf6008dee8.png">
출처: 도서 [파이썬으로 살펴보는 아키텍처 패턴]

<br>

### 문제 상황
기존 운영하던 A서버의 레이어가 Controller - Service 로만 구성되어 있었고, 아래와 같은 문제가 있었음

- 비즈니스 로직과 DB접근 로직이 강하게 결합되어 있음 
  - 코드의 복잡도를 높이고, 가독성을 떨어뜨려 변경에 많은 비용이 들게 했다. 
  - 복잡도가 높은 만큼 테스트코드를 작성하는 데에도 어려움이 있었다. 
- 레이어 간 이동하는 데이터의 정보를 알기 어렵다. 
  - 보통 레이어 간 이동에 DTO를 사용하지만 A서버는 Response 데이터 외에 레이어 간 이동에는 dict 를 사용하고 있었다. 
  - 클라이언트로 반환되기 전까지는 데이터의 정보를 알기 어려웠고, 서버의 안정성은 물론 개발 생산성에도 부정적인 영향을 미쳤다. 
  - 데이터 정보에 대한 문제는 설계와 별개였지만, 저장소 패턴을 도입하면서 함께 해결하기로 함 
<br>

### 개선 방향 

서비스에서 DB 접근 로직을 분리하자!
Repository 레이어를 추가하고 추상화된 인터페이스에 의존함으로써 "비즈니스 로직에만 집중"할 수 있는 구조를 만들자 
DTO를 사용해 데이터의 값과 타입을 명확하게 명시하자 

<br>

### 결과

Service 와 Repository 레이어를 분리하고 인터페이스를 사용하여 결합도를 낮춘 유연한 구조를 만들었다. 
DTO 를 통해 데이터가 어느 레이어에 있든 '값'과 '타입'을 확인할 수 있게 되었다. 
<br>
저장소 패턴 적용
```python
import abc 

# 인터페이스 클래스 
class Repository(abc.ABC):
  @abc.abstractmethod
  def get_name(self, user_id):
    ... 
  
# 구현 클래스
class NameRepository(Repository):
  def get_name(self, user_id):
    # DB 접근 로직 구현 
    pass 
    
# 분리 전, 서비스 레이어
def get_name(user_id):
  query = select(name).where(user.id==user_id)
  name = fetch(query)
  return name

# 분리 후
import NameRepository

def get_name(user_id):
  repo = NameRepository() 
  name = repo.get_name(user_id)
  return name 

# 저장소 인터페이스를 컨트롤러 레이어에서부터 주입받아 의존관계 주입을 구현하였다.
# 의존관계 주입 : 기존 단방향이던 의존관계를, 외부 주입을 통해 상위모듈과 하위모듈이 모두 추상화된 인터페이스를 의존하도록 만드는 것이다.
def get_name(repo, user_id):
  name = repo.get_name(user_id)
  return name 
```
<br>

DTO 적용 과정
단점 : DTO 를 생성하는 코드가 반복된다.

```python
from dataclasses import dataclass 

@dataclass
class NameDto:
  name: str 

class NameRepository(Repository):
  def get_name(self, user_id):
    ...
    data = fetch(query)
    name = NameDto(name=data['name'])
    return name 
```
<br>

#### 참고
- https://daco2020.tistory.com/m/439<br>
- https://0391kjy.tistory.com/39<br>
- https://velog.io/@khh180cm/2.-%EC%A0%80%EC%9E%A5%EC%86%8C-%ED%8C%A8%ED%84%B4<br>
