## Django 에서 쿼리셋 효과적으로 사용하기

ORM 을 효과적으로 사용한다 = ORM이 쿼리를 어떻게 작성하는지 이해한다.
<br>

### Django 의 쿼리는 마지막까지 지연(lazy) 된다.

DB의 레코드를 진짜로 fetch하려면, 쿼리셋을 순회(iterate) 해야한다.

```python
person_set = Person.objects.filter(name="Hyejin")  # 아직 DB에 어떤 쿼리도 전달하지 않는다.

for person in person_set:  
  print(person.name)
```
<br>

### Django 의 쿼리셋은 캐시된다.

평가 : DB 레코드들을 실제로 fetch 한 후 모두 Django 모델로 변환된다. 

평가된 모델들은 쿼리셋의 내장 캐시에 저장되므로, 쿼리셋을 다시 순회하더라도 같은 쿼리를 또 전달하지 않는다. 

```python
person_set = Person.objects.filter(name="Hyejin")

# 쿼리가 '평가'되고, 결과가 캐시된다.
for person in person_set: 
  print(person.name)
  
# 똑같은 순회를 반복하면, 이미 캐시된 쿼리셋이 사용된다.
for person in person_set:
  print(person.age)
```
<br>

### if 문에서 쿼리셋 평가가 발생한다.

```python
person_set = Person.objects.filter(name="Hyejin")

# if 문은 쿼리셋을 '평가'한다.
if person_set:
  # 순회할 때는 캐시된 쿼리셋이 사용된다.
  for person in person_set:
    print(person.name)
```
<br>

**결과 전체가 필요하지 않은 경우, 쿼리셋 캐시가 문제가 된다.**

```python
person_set = Person.objects.filter(name="Hyejin")

# if 문은 쿼리셋을 '평가'한다. - (불필요하다)
if person_set:
  print('Exists!')
```
<br>

**이것을 피하려면, exists() 메서드를 사용하자.**

```python
person_set = Person.objects.filter(name="Hyejin")

# exists() 는 쿼리셋 캐시를 만들지 않으면서, 레코드의 유무를 검사한다. 
if person_set.exists():
  print('Exists!')
```
<br>

### 쿼리셋이 엄청 큰 경우, 쿼리셋 캐시가 문제가 된다.

몇천개 단위의 레코드를 다뤄야할 경우, 이 데이터를 한번에 가져와 메모리에 올리는 행위는 매우 비효율적이다.

거대 쿼리가 서버의 프로세스를 잠궈(lock) 버려서 웹어플리케이션이 죽을 수도 있다.

쿼리셋 캐시를 방지하면서 전체 레코드를 순회해야 한다면, **iterator()** 를 사용하자. 

데이터를 작은 덩어리로 쪼개어 가져오고, 이미 사용한 레코드는 메모리에서 지운다. 

iterator() 메서드를 사용하면, 같은 쿼리셋을 다시 순회할 때 쿼리를 다시 평가한다. 
<br>

**같은 거대 쿼리셋을 재사용하려고 하지 않는지 주의해야 한다.**

```python
person_set = Person.objects.all()

# iterator() 메서드는 전체 레코드의 일부씩만 DB에서 가져온다. 
# 메모리를 절약할 수 있다. 
for person in person_set.iterator():
  print(person.name)
```
<br>

### 쿼리셋이 엄청 큰 경우 if 문도 문제가 된다.

쿼리셋이 엄청 큰 경우, 쿼리셋 캐시는 고려사항이 될 수 없다. 

해결책 1) exists() 와 iterator() 를 함께 사용

두개의 쿼리를 실행하는 대신 쿼리셋 캐시로 생성하는 일을 방지할 수 있다. 

```python
person_set = Person.objects.all()

# 첫 번째 쿼리로, 쿼리셋에 레코드가 존재하는지 확인한다. 
if person_set.exists():
  # 또다른 쿼리로 레코드를 조금씩 가져온다.
  for person in person_set.iterator():
    print(person.name)
```

해결책2) 파이썬의 고급 순회 메서드 (advanced iteration methods) 사용 

순회를 진행할지 결정하기 전에 iterator() 메서드의 첫번째 레코드를 감지(peek)할 수 있다. 

```python
person_set = Person.objects.all()

# 첫번째 쿼리로 레코드를 가져오기 시작한다.
person_iterator = person_set.iterator() 

# 첫번째 레코드를 감지(peek)한다.
try:
  first_person = next(person_iterator)
except StopIteration:
  # 레코드가 없다면 아무일도 하지 않는다. 
  pass 
else:
  # 레코드가 하나라도 존재한다면,
  # 모든 레코드를 순회한다. 
  from itertools import chain
  for person in chain([first_person], person_set):
    print(person.name)
```
주의<br>

- 쿼리셋 캐시는 DB쿼리의 수를 줄이며 정말로 필요한 쿼리만을 DB에 전달하기 위해 존재한다. 
- exists()와 iterator() 메서드를 사용하면 메모리 사용을 최적화할 수 있다. 
- 그렇지만 쿼리셋 캐시는 생성되지 않기 때문에, DB 쿼리가 중복될 수 있다.
