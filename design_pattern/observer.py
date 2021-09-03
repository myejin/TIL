class Observer:
    """
    데이터 변경을 통보받는 클래스
    Subject 에서는 Observer의 update 메소드를 호출하여 통보한다.
    """

    def update(self):
        pass


class Subject:
    """Observer 객체들을 관리하는 요소"""

    def __init__(self):
        self.observers = []

    def add_o(self, o: Observer):
        self.observers.append(o)

    def delete_o(self, o: Observer):
        self.observers.remove(o)

    def notify_to_observers(self):
        for o in self.observers:
            o.update()


class ScoreBoard(Subject):
    """
    통보하는 클래스
    setter(add_score)를 통해 데이터(상태)를 변경시킨다.
    notify를 통해 Observer에 변경내용을 통보한다.
    """

    def __init__(self):
        super().__init__()
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)
        self.notify_to_observers()

    def get_scores(self):
        return self.scores


class DataSheetView(Observer):
    """
    실제 통보받는 클래스
    상위클래스인 Observer의 update 메소드를 오버라이딩하여 통보받는다.
    통보하는 클래스의 get_state 메소드를 호출하여 변경을 조회한다.
    """

    def __init__(self, score_board, viewcount):
        super().__init__()
        self.score_board = score_board
        self.viewcount = viewcount

    def update(self):
        super().update()
        scores = self.score_board.get_scores()
        self.display_scores(scores, self.viewcount)

    def display_scores(self, scores, viewcount):
        if not scores:
            print("저장된 점수가 없습니다.")
            return

        print(f"총 {viewcount}개의 점수데이터 : ", end="")
        for i, score in enumerate(scores):
            if i == viewcount:
                break
            print(score, end=" ")
        print()


class MinMaxView(Observer):
    def __init__(self, score_board):
        super().__init__()
        self.score_board = score_board

    def update(self):
        super().update()
        scores = self.score_board.get_scores()
        self.display_scores(scores)

    def display_scores(self, scores):
        if not scores:
            print("저장된 점수가 없습니다.")
            return
        m = min(scores)
        M = max(scores)
        print(f"min : {m} | Max : {M}")


class AverageView(Observer):
    def __init__(self, score_board):
        super().__init__()
        self.score_board = score_board

    def update(self):
        super().update()
        scores = self.score_board.get_scores()
        self.display_scores(scores)

    def display_scores(self, scores):
        if not scores:
            print("저장된 점수가 없습니다.")
            return
        print(f"평균점수는 {sum(scores) // len(scores)}")


if __name__ == "__main__":
    observer = Observer()
    subject = Subject()
    score_board = ScoreBoard()
    view1 = DataSheetView(score_board, 3)
    view2 = MinMaxView(score_board)

    for s in range(10, 101, 10):
        score_board.add_score(s)

    view1.update()
    view2.update()

    view3 = AverageView(score_board)
    view3.update()
