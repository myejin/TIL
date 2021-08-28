from concurrent import futures
import time


def work():
    time.sleep(1)
    # return "Done"


if __name__ == "__main__":
    print("[싱글스레드]")
    start = time.perf_counter()
    for _ in range(10):
        work()
    finish = time.perf_counter()
    print(f"총 {round(finish-start, 2)} 초 걸렸습니다.")

    print("\n[멀티스레딩]")
    start = time.perf_counter()

    with futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(work) for _ in range(10)]

    # for f in futures.as_completed(results):
    #     print(f.result())

    finish = time.perf_counter()
    print(f"총 {round(finish-start, 2)} 초 걸렸습니다.")
