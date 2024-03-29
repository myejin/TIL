## 0. 스레드(Thread)?

- 프로세스 내의 실행 흐름 단위
  - Chrome(프로세스) 에서 Youtube 시청(스레드1)하면서 웹 서핑(스레드2)을 한다?
- 스레드는 프로세스에 할당된 메모리, CPU 등 자원을 사용한다.
- 메모리(Code, Data, Heap, Stack) 영역 중 Stack 만 별도로 할당한다.
- 한 스레드의 결과는 다른 쓰레드에 영향을 끼친다.
<br><br>


## 1. 멀티 스레드

- 멀티프로세스에 비해, 
  - 시스템 자원소모를 감소시키고 처리량을 증가시킨다.
  - 스레드 간 통신이 더 쉽다.
  - 디버깅이 어렵기 때문에 <b>자원 공유 문제(교착상태)</b>는 주의해서 구현하자.
<br><br>


## 2. threading 모듈 활용
- 일련의 코드를 다른 스레드에서 실행한다.
  - 단일 스레드에서 메인루틴이 서브루틴을 호출하는 경우, 서브루틴의 작업이 완료되기 전까지 메인루틴이 멈추게 된다.
  - 이때 서브루틴의 코드가 별도의 스레드에서 작동한다면, 메인루틴은 방해받지 않는다.
- `(concurrent.futures와 차이점)` 서브루틴의 결과를 메인스레드(또는 원래 스레드)로 전달하지 않는다.
  - 두 스레드 간 데이터 전달은 별도의 queue 모듈을 사용해야 한다.
<br>

```python
def work(name):
    """스레드에서 실행할 함수"""
    logging.info(f"[Sub-thread] {name}: 시작합니다.")
    time.sleep(3)
    logging.info(f"[Sub-thread] {name}: 종료합니다.")


if __name__ == "__main__":
    <...생략...>

    x = Thread(target=work, args=("A",))
    logging.info("[Main-Thread] 쓰레드 시작 전")
    x.start()
    logging.info("[Main-Thread] 프로그램 종료합니다.")
```

- `if __name__ == "__main__"` : 메인스레드 흐름을 타는 시작점

- `Thread(target=work, args=("A",))`

  - `target` : 스레드가 실행할 함수(callable object) 지정

- 결과

  ```
  22:24:09: [Main-Thread] 쓰레드 시작 전
  22:24:09: [Sub-thread] A: 시작합니다.       
  22:24:09: [Main-Thread] 프로그램 종료합니다.
  22:24:12: [Sub-thread] A: 종료합니다.
  ```

  - 메인스레드 종료 후에도 서브스레드가 마무리된다.<br><br>

:bulb: 서브스레드가 종료될 때까지 메인스레드는 기다릴 수 없나? :heavy_check_mark: `join()` 

```python
if __name__ == "__main__":
    <...생략...>

    x = Thread(target=work, args=("A",))
    logging.info("[Main-Thread] 쓰레드 시작 전")
    x.start()
    logging.info("[Main-Thread] 쓰레드 종료를 기다립니다.")  # 추가된 부분1
    x.join()  # 추가된 부분2
    logging.info("[Main-Thread] 프로그램 종료합니다.")
```

- 결과

  ```
  22:34:49: [Main-Thread] 쓰레드 시작 전
  22:34:49: [Sub-thread] A: 시작합니다.
  22:34:49: [Main-Thread] 쓰레드 종료를 기다립니다.
  22:34:52: [Sub-thread] A: 종료합니다.
  22:34:52: [Main-Thread] 프로그램 종료합니다.
  ```

  - 메인스레드도 3초후 종료되었다.<br><br>

:bulb: 데몬 스레드 

- 메인스레드가 종료되면 즉시 종료되는 스레드
- 백그라운드에서 실행된다.

- <a href="https://github.com/myejin/TIL/blob/master/Thread/threading_test.py">:memo: 코드</a>  

- 결과

  - 일반스레드 `A`는 1 - 9 만큼 출력한다.
  - 데몬스레드 `D`는 다 출력되지 못한 채 에러가 발생했다.
  - 테스트할 때 정상적으로 수행되기도 하는데, 이 경우 r의 범위를 크게 하면 에러가 발생한다.
  <br>

  ```
  22:37:23: [Main-Thread] 쓰레드 시작 전
  22:37:23: [Sub-thread] A: 시작합니다.
  22:37:23: [Sub-thread] D: 시작합니다.
  A 0
  22:37:23: [Main-Thread] 프로그램 종료합니다.
  A 1
  A 2
  D 0
  A 3
  D 1
  A 4
  D 2
  A 5
  D 3
  A 6
  A 7
  D 4
  A 8
  D 5
  A 9
  22:37:23: [Sub-thread] A: 종료합니다.
  D 6
  ```

- 에러메세지

  ```
  Fatal Python error: _enter_buffered_busy: could not acquire lock for <_io.BufferedWriter name='<stdout>'> at interpreter shutdown, possibly due to daemon threads
  Python runtime state: finalizing (tstate=00000211C3D50F60)
  
  Current thread 0x00005df4 (most recent call first):
  <no Python frame>
  ```


<br>

:bulb: 싱글스레드와 비교

- `time.sleep(1)` 걸리는 함수 10번 실행

- <a href="https://github.com/myejin/TIL/blob/master/Thread/thread.py">:memo:코드</a>

- 결과

  ```
  [싱글스레드]
  총 10.08 초 걸렸습니다.
  
  [멀티스레딩]
  총 1.02 초 걸렸습니다.
  ```
<br><br>

## 3. concurrent.futures 모듈 활용

- `3.2 버전부터 도입` 

- 스레드와 프로세스를 처리하는 API가 통일되었다. 
- 비동기 코루틴과 <b>거의 유사한</b> 형태의 API 제공 
  - (주의) `concurrent`와 `asyncio`의 Future는 호환되는 클래스는 아니다.
- 병렬처리 API 
  - `Executor` : 함수호출을 비동기로 디스패치하는 클래스 
    - 스레드/프로세스를 생성하고 작업을 스케줄링 한다.
    - 스레드와 프로세스를 처리하는 API가 같기 때문에, 실행기만 선택해주면 멀티스레드/멀티프로세스 환경으로 쉽게 변경할 수 있다. 
      - - `ThreadPoolExecutor`, `ProcessPoolExecutor` 중 하나 선택 
  
  - `Future` : 별도의 실행흐름에서 처리되는 코드를 캡슐화한 것
    - 태스크가 어디선가 처리중이며, <b>'미래의 적절한 시점에 결과가 resolve되어 나온다'</b>는 것을 보장한다.
    - 다른 스레드에서 작동한 코드가 만드는 결과물을 (원래 스레드로) 안전, 용이하게 전달받을 수 있다.
    - 스레드가 작업을 스케줄링한 후, 즉시 `Future` 객체를 얻게된다.
    - 실행 중인 병렬작업 취소, 실행 진행/완료 여부 체크, 타임아웃 설정, 완료콜백 추가 등
    - JS의 비동기 태스크 프로토콜인 `Promise`와 유사함
  - 모듈함수 : `.wait()`, `.as_completed()` 등 함수를 통해 병렬처리 결과를 동기화할 수 있다.(Future 객체를 얻게된다.)<br>

<br>

:bulb: 멀티스레딩 구현 

```python
def work():
    time.sleep(1)

if __name__ == "__main__":
    print("\n[멀티스레딩]")
    start = time.perf_counter()

    with futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(work) for _ in range(10)]

    finish = time.perf_counter()
    print(f"총 {round(finish-start, 2)} 초 걸렸습니다.")
```

- <a href="https://github.com/myejin/TIL/blob/master/Thread/concurrent_test.py">:memo:전체코드</a> 
- 스레드 풀 생성
  - `futures.ThreadPoolExecutor` 클래스의 인스턴스 `executor` 생성

- 스레드 풀에 작업(함수) 제출

  - `submit` : 개별 함수의 호출을 별도의 흐름에서 시작하고, 즉시 Future 객체를 반환한다.
    - (참고) `map()`은 여러 작업을 동시에 시작할 때 사용한다.

- 결과

  ```
  [멀티스레딩]
  총 1.03 초 걸렸습니다.
  ```
<br>

:bulb: 멀티스레드로 구현해도 수행시간이 줄지 않는다?

```python
def work(r):
    res = 0
    for i in r:
        res += i
    return res


if __name__ == "__main__":
    print("[싱글스레드]")
    start = time.perf_counter()

    results = work(range(1, 100000000))
    print("work 결과 : ", results)

    finish = time.perf_counter()
    print(f"총 {round(finish-start, 2)} 초 걸렸습니다.")

    print("\n[멀티스레딩]")
    start = time.perf_counter()

    with futures.ThreadPoolExecutor() as executor:
        sub_range = [range(1, 100000000 // 2), range(100000000 // 2, 100000000)]
        results = executor.map(work, sub_range)  # 부분합을 구한 후
    print("work 결과 : ", sum(results))  # 다시 합친다.

    finish = time.perf_counter()
    print(f"총 {round(finish-start, 2)} 초 걸렸습니다.")
```

- <a href="https://github.com/myejin/TIL/blob/master/Thread/concurrent_test2.py">:memo:전체코드</a> 

- `map`

  - 결과에 대한 제너레이터 반환
  - 타임아웃을 별도 지정하지 않으면, 모든 작업이 종료될 때까지 기다린 후 리턴
  - 타임아웃 작업이 완료되지 못하면, 예외 발생
  
- 결과

  ```
  [싱글스레드]
  work 결과 :  4999999950000000
  총 4.51 초 걸렸습니다.
  
  [멀티스레딩]
  work 결과 :  4999999950000000
  총 4.35 초 걸렸습니다.
  ```

- 이유 :heavy_check_mark: `파이썬 정책, GIL(Global Interpreter Lock)`  

  - 한 순간에 하나의 스레드만 동작한다.
    - CPU 분산 처리의 효과를 누릴 수 없다.
    - 작업 단위를 쪼개도, 하나의 스레드 작업이 완료되어야 다른 스레드가 일을 할 수 있다.
    
  - CPU 작업이 적고, I/O 작업이 많은 경우에 효과적이다.
    - 파일쓰기의 경우 I/O 작업이 아니어서 오히려 시간이 더 걸린다.(컨텍스트 스위칭 때문):weary: 
<br>

:bulb: CPU 부하가 많은 작업을 분산처리 하려면, `ProcessPoolExecutor` 사용하자!

- 결과

  ```
  [싱글스레드]
  work 결과 :  4999999950000000
  총 4.46 초 걸렸습니다.
  
  [멀티프로세싱]        
  work 결과 :  4999999950000000
  총 2.69 초 걸렸습니다.
  ```





