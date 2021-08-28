from concurrent import futures
import time


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
