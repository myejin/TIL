import asyncio
import time
import os


async def co_work(r, loop, executor=None):
    print(f"{os.getpid()} | {time.strftime('%X')} : hi")
    await loop.run_in_executor(executor, sum, r)
    print(f"{os.getpid()} | {time.strftime('%X')} : bye")


async def coroutine_main():
    r = [range(1, 500000000 // 2), range(500000000 // 2, 500000000)]
    loop = asyncio.get_event_loop()
    print(f"{os.getpid()} | {time.strftime('%X')} : coroutine_main 시작")
    await asyncio.gather(co_work(r[0], loop), co_work(r[1], loop))
    print(f"{os.getpid()} | {time.strftime('%X')} : coroutine_main 종료")


if __name__ == "__main__":

    print("\n[비동기]")
    start = time.perf_counter()
    asyncio.run(coroutine_main())
    finish = time.perf_counter()
    print(f"총 {round(finish-start, 2)} 초 걸렸습니다.")
