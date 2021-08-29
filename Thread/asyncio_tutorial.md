## :bulb: 네이티브 코루틴

- `python 3.5`에서 코루틴을 명시적으로 지정하는 `async/await ` 키워드 추가
- <a href="https://wikidocs.net/16069" style="text-decoration:none">제너레이터 기반 코루틴 (함수 내 yield 유무로 결정)</a>과 비교하기 위한 개념
- 코루틴 호출만으로 실행이 예약되는 것은 아니다.



#### 예제1 

```python
import asyncio
import time

async def say_after(delay, data):
    await asyncio.sleep(delay)
    print(f"{time.strftime('%X')} : {data}")

async def main():
    print(f"{time.strftime('%X')} : 시작")
    await say_after(1, "hello")
    await say_after(2, "world")
    print(f"{time.strftime('%X')} : 종료")

asyncio.run(main())  # 최상위 진입점 main() 함수 실행 
print(main())
```

#### 결과 

- 순차적으로 함수 실행 (총 <b>3초</b> 소요)

```
22:11:05 : 시작
22:11:06 : hello
22:11:08 : world
22:11:08 : 종료
<coroutine object main at 0x0000020F996C3240>
```

<br>

#### 예제2

- 두 개의 `say_after` 코루틴을 동시에 실행하기

- `create_task()` : 코루틴을 비동기 태스크로 동시에 실행하는 함수

```python
<...생략..위와 동일...>

async def main():
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"{time.strftime('%X')} : 시작")
    await task1
    await task2
    print(f"{time.strftime('%X')} : 종료")

asyncio.run(main())
```

#### 결과

- `task1` 과 `task2`가 동시 실행 (총 <b>2초</b> 소요)

```
22:20:20 : 시작
22:20:21 : hello
22:20:22 : world
22:20:22 : 종료
```

<br><br>

## :bulb: 어웨이터블

- 어웨이터블 객체 : `await` 표현식에서 사용될 수 있는 객체 
  - 세가지 유형 : `코루틴`, `태스크`, `퓨처` 

<br>

#### 코루틴(Coroutine)

> 코루틴 함수 : async def 함수
>
> 코루틴 객체 : 코루틴 함수를 호출하여 반환된 객체

```python
import asyncio

async def nested():
    return 42

async def main():
    nested()  # ----(1)
    print(await nested())  # ----(2)

asyncio.run(main())
```

- `(1) nested()`를 호출하면 아무 일도 일어나지 않는다.

  - 코루틴 객체지만, 기다리지 않는다 + 전혀 실행되지 않는다.

- `(2) nested()` 는 42를 반환한다.<br>

- 결과 (Python 3.9)

  ```
  RuntimeWarning: coroutine 'nested' was never awaited nested()
  RuntimeWarning: Enable tracemalloc to get the object allocation traceback   
  42
  ```

<br>

#### 태스크(Task)

- 코루틴을 동시에 예약하는 데 사용된다.
  - 코루틴이 `create_task()` 함수를 사용하여 <b>태스크</b>로 감싸지면, 코루틴이 곧 실행되도록 자동으로 예약된다.
- :memo: [예제2 코드 참고](#예제2)

<br>

#### 퓨처(Future)

- 비동기 연산의 <b>최종 결과</b>를 나타내는 <b>저수준</b> 어웨이터블 객체
- Future 객체 기다린다?
  - 코루틴이 Future가 다른 곳에서 해결될 때까지 기다리는 것
- async/await 와 <b>콜백 기반 코드</b>를 함께 사용하려면 asyncio의 Future 객체가 필요하다. 
- `concurrent` (python 3.2) 방식의 `future` ? <a href="https://github.com/myejin/TIL/blob/master/Thread/%EB%A9%80%ED%8B%B0%EC%8A%A4%EB%A0%88%EB%93%9C.md" style="text-decoration:none"> :heavy_check_mark: `이해하기`</a> 

<br><br>

### :bulb: asyncio 메소드

#### <b> `gather`</b>(*aws, loop=None, return_exceptions=False)

- aws 시퀀스에 있는 어웨이터블 객체를 <b>동시에 실행</b>한다.
- aws 에 있는 어웨이터블이 코루틴이면 자동으로 태스크로 예약된다.
- 모든 어웨이터블이 성공적으로 완료되면
  - 결과 : 반환값들이 합쳐진 리스트
- return_exceptions가 `False`(default) 면, 첫번째 발생한 예외가 `gather()`를 기다리는 태스크로 즉시 전파된다.
  - 다른 어웨이터블은 취소되지 않고 계속 실행된다.
  - `True`라면, 예외는 성공적인 결과처럼 처리된다.
- `gather()` 가 취소되면, 모든 제출된 (아직 완료되지 않은) 어웨이터블도 취소된다.
- aws 시퀀스의 태스크나 퓨처가 취소되면, `CancelledError`를 일으킨 것처럼 처리된다.
  - `gather()` 호출은 취소되지 않는다.
  - 태스크/퓨처가 연쇄적으로 취소되는 것을 막는다.

#### 예제

```python
import asyncio
import time

async def factorial(name, num):
    f = 1
    print(f"{time.strftime('%X')} | 태스크 {name} : factorial({num}) 실행시작")
    for i in range(2, num + 1):
        await asyncio.sleep(1)
        f *= i
    print(f"{time.strftime('%X')} | 태스크 {name} : factorial({num}) = {f}")
    return f

async def main():
    L = await asyncio.gather( # 자동으로 태스크로 예약
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())
```

#### 결과

```
23:22:30 | 태스크 A : factorial(2) 실행시작
23:22:30 | 태스크 B : factorial(3) 실행시작
23:22:30 | 태스크 C : factorial(4) 실행시작
23:22:31 | 태스크 A : factorial(2) = 2
23:22:32 | 태스크 B : factorial(3) = 6
23:22:33 | 태스크 C : factorial(4) = 24
[2, 6, 24]
```

<br>

---

(..공부중..)

#### <b> `shield`</b> (*aws, loop=None)

- 어웨이터블 객체를 취소로부터 보호합니다.
- 





### 참고

- <a href="https://docs.python.org/ko/3/library/asyncio-task.html"> `https://docs.python.org/ko/3/library/asyncio-task.html`</a>

