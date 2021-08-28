import logging
from threading import Thread


def work(name, r):
    """스레드에서 실행할 함수"""
    logging.info(f"[Sub-thread] {name}: 시작합니다.")
    for i in r:
        print(name, i)
    logging.info(f"[Sub-thread] {name}: 종료합니다.")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    x = Thread(target=work, args=("A", range(10)))
    d = Thread(target=work, args=("D", range(10)), daemon=True)

    logging.info("[Main-Thread] 쓰레드 시작 전")
    x.start()
    d.start()
    logging.info("[Main-Thread] 프로그램 종료합니다.")
