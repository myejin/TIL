my_list = list(range(8))  # 0 ~ 7
tree = [0] * 16


def init(left, right, node):
    """구간합 세그먼트 트리 초기화"""
    print(left, right, node)
    if left == right:
        tree[node] = my_list[left]
        print(f"리프노드 N{node} {tree[node]}")
        return
    else:
        mid = (left + right) // 2
        init(left, mid, node * 2)
        init(mid + 1, right, node * 2 + 1)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        print(f"{left}~{right} 구간합 (N{node}) {tree[node]}")


def update(left, right, node, idx, value):
    """idx 에 해당하는 값을 value로 변경, 그로인해 바뀌는 구간합도 업데이트"""
    print(left, right, node, idx, value)
    if left == right == idx:
        tree[node] = value
        print(f"인덱스 {idx} 찾았다! {value}로 변경")
        return
    if idx < left or right < idx:
        print("구간에 해당되지 않는다")
        return
    else:
        mid = (left + right) // 2
        update(left, mid, node * 2, idx, value)
        update(mid + 1, right, node * 2 + 1, idx, value)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        print(f"업데이트 반영 N{node} {tree[node]}")


def query(left, right, node, lidx, ridx):
    """lidx ~ ridx 구간합 조회"""
    global answer
    print(left, right, node, lidx, ridx, answer)
    if ridx < left or right < lidx:
        print("구간에 해당되지 않는다")
        return
    elif lidx <= left and right <= ridx:
        answer += tree[node]
        print(f"{lidx}~{ridx} 에 포함되는 구간이다!")
        return
    elif lidx <= right or left <= ridx:
        mid = (left + right) // 2
        query(left, mid, node * 2, lidx, ridx)
        query(mid + 1, right, node * 2 + 1, lidx, ridx)
        print("교집합이 존재한다. 범위를 더 쪼개자!")
        return


if __name__ == "__main__":
    init(0, 7, 1)
    b = input()

    update(0, 7, 1, 3, 10)
    b = input()

    answer = 0
    query(0, 7, 1, 2, 5)
    print(answer)
    b = input()

    answer = 0
    query(0, 7, 1, 3, 4)
    print(answer)
    b = input()
