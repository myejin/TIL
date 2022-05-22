## HackSoft Django Style-guide

>`https://github.com/HackSoftware/Django-Styleguide/blob/master/README.md` 를 읽고 정리한다.
<br>

### 🔴 Overview
비즈니스 로직을 어느 위치에 작성하는 것이 좋을까?

✔️ <b>좋은 예</b>

- DB에 write - Service (= `커스텀된 Manager, Queryset` + `도메인을 별도로 유지` )
- DB로부터 fetch - Selectors
- Model properties
  - 여러 릴레이션에 걸쳐있거나 쉽게 `N+1`쿼리 문제를 일으킨다면, Selectors
- 추가 validation - 모델의 `clean` 메소드
<br>

✔️ <b>좋지 못한 예</b>

- API 및 View / Serializer 및 Form / Form 태그 / 모델의 `save` 메소드 
  - 비즈니스 로직을 여러 위치에 파편화하기 때문에, 데이터 흐름을 추적하기 어렵다.
  - 무언가를 변경하려면 추상화된 내부동작을 이해해야 한다.
- 커스텀된 Manager, Queryset 
  - 비즈니스 로직에는 데이터모델에 직접 매핑되지 않는 자체 도메인이 항상 있다.
  - 비즈니스 로직은 대부분 여러 모델에 걸쳐있다. 모델 A, B, C, D 중 어디에 넣을지?
  - 써드-파티로 추가 호출이 있을 수 있다. 
- Signal
  - 서로에 대해 알지 못하지만 연결이 되어야할 때 사용된다.
  - 비즈니스 논리 계층 외부에서 캐시 무효화를 처리하는 데 사용된다. 
<br>

---

### 🟡 Models



### Services



### APIs & Serializers



### Errors & Exception Handling 



### Testing 







