## Generator, 제너레이터

- 함수의 실행을 일시 중지하고, 여러 값을 생성할 수 있는 함수
- 어떤 하나의 값을 반환하지 않는다.

```python
def my_gen():
    yield "Hello"
    yield "World"

gen = my_gen()
# 어떤 값도 직접 반환하지 않는다.
# 호출되면 제너레이터 객체를 전달한다.
print(gen)
print(next(gen))
print(next(gen))
```

- 결과

```
<generator object my_gen at 0x0000021E8D139510>
Hello
World
```

<br>

- 장점 : 메모리를 효율적으로 사용
  - next() 메소드를 통해 차례로 값에 접근할 때마다 메모리에 적재하는 방식

```python
import sys

print(sys.getsizeof((i for i in range(100))))  # 112
print(sys.getsizeof((i for i in range(10000))))  # 112
```

<br><br>

## Coroutine, 코루틴

- 제너레이터에 데이터를 푸시하고 싶다면?  :heavy_check_mark: `코루틴` 
  - 제너레이터가 데이터 만드는 것 말고
  - 외부에서 제공되는 데이터를 소비하는 역할

<br>

- 제너레이터 기반 코루틴
  - 값을 받는데 사용하는 `yield` 키워드를 "="의 우축 표현식으로 사용
  - `send()` 메소드를 사용해 값을 함수로 전달 

```python
def coro():
    hello = yield "Hello"
    yield hello

c = coro()
print(c)
print(next(c))  # 값을 가져온다.
print(c.send("World"))  # 함수를 다시 시작하고 hello에 "World"을 할당한 후 다음 yield 실행한다.
```

- 결과

```
<generator object coro at 0x0000018568799510>
Hello
World
```

<br><br>

## asyncio 모듈

- `python 3.4`
- 이 모듈과 코루틴을 함께 사용하여 비동기 IO를 쉽게 수행할 수 있다.

```python
import asyncio
import datetime

@asyncio.coroutine
def display_date(name, loop):  # 코루틴 함수
    end_time = loop.time() + 5.0
    while True:
        print(f"{name} {datetime.datetime.now()}")
        if (loop.time() + 1.0) >= end_time:
            break
        # 외부로부터 값을 받아올 수 있다.
        # yield from이 함수(sleep())호출의 결과를 기다린다.
        # yield from을 사용할 때, 이벤트 루프가 해당 코루틴의 실행을 일시 중지한다.
        yield from asyncio.sleep(1)

loop = asyncio.get_event_loop()
asyncio.ensure_future(display_date("A", loop))
asyncio.ensure_future(display_date("B", loop))
loop.run_forever()  # 루프가 계속 실행되도록 요청
```

- 결과

```
A 2021-08-31 00:50:41.707248
B 2021-08-31 00:50:41.708257
A 2021-08-31 00:50:42.712584
B 2021-08-31 00:50:42.712584
A 2021-08-31 00:50:43.725152
B 2021-08-31 00:50:43.725152
A 2021-08-31 00:50:44.732472
B 2021-08-31 00:50:44.733457
A 2021-08-31 00:50:45.744800
B 2021-08-31 00:50:45.744800
```

<br>

- `python 3.5`
- `async/await` 키워드로 네이티브 코루틴 구현 
- 제너레이터 기반 코루틴과 기능상의 차이점은 없지만, 구문을 혼용할 수는 없다.
  - 상호 운영하려면? ​ :heavy_check_mark: `@types.coroutine` 데코레이터 추가

<br>

<br>

## 참고

- <a href="https://hamait.tistory.com/830"> `https://hamait.tistory.com/830`</a>

