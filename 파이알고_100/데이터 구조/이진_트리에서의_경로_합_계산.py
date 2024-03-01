def solution(data):
    tree = data["tree"]
    if not tree:
        return []

    # 루트 노드와 그 값을 튜플로 묶음
    stack = [(tree, tree["value"])]
    # [
    #     (
    #         {
    #             "value": 1,
    #             "left": {"value": 2, "left": {"value": 4}, "right": {"value": 5}},
    #             "right": {"value": 3},
    #         },
    #         1,
    #     )
    # ]

    # 각 경로의 합을 저장할 리스트
    path_sums = []

    # 스택이 빌 때까지 반복
    while stack:
        current, current_sum = stack.pop()

        # 현재 노드가 리프 노드인 경우, 경로 합을 결과에 추가
        if not current.get("left") and not current.get("right"):
            path_sums.append(current_sum)

        # 오른쪽 자식이 있으면 스택에 추가
        if current.get("right"):
            stack.append((current["right"], current_sum + current["right"]["value"]))

        # 왼쪽 자식이 있으면 스택에 추가
        if current.get("left"):
            stack.append((current["left"], current_sum + current["left"]["value"]))

    return path_sums


solution(
    {
        "tree": {
            "value": 1,
            "left": {"value": 2, "left": {"value": 4}, "right": {"value": 5}},
            "right": {"value": 3},
        }
    }
)
