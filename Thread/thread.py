from threading import Thread
import threading
import time


def work():
    time.sleep(1)


if __name__ == "__main__":
    print("[싱글스레드]")
    start = time.perf_counter()
    for _ in range(10):
        work()
    finish = time.perf_counter()
    print(f"총 {round(finish-start, 2)} 초 걸렸습니다.")

    print("\n[멀티스레딩]")
    start = time.perf_counter()
    threads = []
    for _ in range(10):
        t = Thread(target=work)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    finish = time.perf_counter()
    print(f"총 {round(finish-start, 2)} 초 걸렸습니다.")
