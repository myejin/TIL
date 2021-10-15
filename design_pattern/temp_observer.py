class Observer:
    """상태변화를 알아야하는 관찰 객체"""

    def __init__(self, publisher, name):
        self.publisher = publisher
        publisher.add(self)
        self.name = name
        self.title_news = ""

    def update(self, genre, title, news):
        """타이틀과 뉴스를 추가한다."""
        self.title_news = f"!{title}!  {news}"
        self.display(genre)

    def display(self, genre):
        print(f"[{self.name}] 오늘의 {genre} 뉴스는?\n{self.title_news}\n")


class DailySubscriber(Observer):
    """매일 뉴스를 구독받는 옵저버"""

    def __init__(self, publisher, name):
        super().__init__(publisher=publisher, name=name)


class EventSubscriber(Observer):
    """이벤트 구독받는 옵저버"""

    def __init__(self, publisher, name):
        super().__init__(publisher=publisher, name=name)


class Publisher:
    """상태를 갖고 있는 주체 객체"""

    def __init__(self):
        self.observers = []

    def add(self, o: Observer):
        """구독을 원하는 옵저버를 등록시킨다."""
        self.observers.append(o)

    def delete(self, o: Observer):
        """구독 명단에서 제외시킨다."""
        self.observers.remove(o)

    def notify_to_observer(self, genre, title, news):
        """옵저버에 새 데이터를 전달한다."""
        for observer in self.observers:
            observer.update(genre, title, news)


class NewsMachine(Publisher):
    """새로운 뉴스를 제공하는 뉴스머신"""

    def __init__(self):
        super().__init__()
        self.genre = ""
        self.title = ""
        self.news = ""

    def set_news(self, genre, title, news):
        self.genre = genre
        self.title = title
        self.news = news
        super().notify_to_observer(genre, title, news)

    def set_it_news(self, title: str, news: str):
        self.set_news("IT", title, news)

    def set_life_news(self, title: str, news: str):
        self.set_news("라이프", title, news)

    def get_title(self):
        if not self.title:
            return "no title yet"
        return self.title

    def get_news(self):
        if not self.news:
            return "no news yet"
        return self.news


if __name__ == "__main__":
    # publisher(subject)) : subscriber = 1 : N
    # N이 계속 늘어남에 따라 클래스를 수정하지 않고, setter 로 데이터만 업데이트한다.
    news_machine = NewsMachine()
    daily_subscriber = DailySubscriber(news_machine, "daily")
    event_subscriber = EventSubscriber(news_machine, "event")

    news_machine.set_life_news("오늘 비 잔뜩 내림", "뭉치 산책 못했습니다.")
    news_machine.set_life_news("치킨 파티", "주식 대박~!")

    # subscriber(옵저버) 인스턴스 추가
    hyejin = DailySubscriber(news_machine, "hyejin")

    # 새로운 뉴스
    news_machine.set_it_news("새로운 뉴스", "옵저버 패턴이란?")
