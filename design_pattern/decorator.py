class Display:
    """
    Component : 기본기능(Concrete)와 추가기능(Decorator)의 공통기능 정의
    """

    def draw(self):
        """추상메소드"""
        pass


class RoadDisplay(Display):
    """ConcreteComponent, 기본기능"""

    def __init__(self):
        super().__init__()

    def draw(self):
        super().draw()
        print("기본 도로 표시")


class DisplayDecorator(Display):
    """추가기능의 구체적인 공통기능 정의"""

    def __init__(self, decorated_display):
        super().__init__()
        self.decorated_display = decorated_display  # 합성할 다른 디스플레이

    def draw(self):
        self.decorated_display.draw()


class LaneDecorator(DisplayDecorator):
    """
    Concrete 객체에 대한 참조가 필요하다.(합성관계)
    합성관계 : 전체객체가 없어지면 부분객체도 없어진다.
    """

    def __init__(self, decorated_display):
        super().__init__(decorated_display=decorated_display)

    def draw(self):
        super().draw()
        print("  + 차선 표시")


class TrafficDecorator(DisplayDecorator):
    def __init__(self, decorated_display):
        super().__init__(decorated_display=decorated_display)

    def draw(self):
        super().draw()
        print("  + 교통량 표시")


if __name__ == "__main__":
    road = RoadDisplay()
    road.draw()

    road_with_lane = LaneDecorator(RoadDisplay())
    road_with_lane.draw()

    road_with_traffic = TrafficDecorator(RoadDisplay())
    road_with_traffic.draw()

    road_with_lane_and_traffic = TrafficDecorator(road_with_lane)
    road_with_lane_and_traffic.draw()
