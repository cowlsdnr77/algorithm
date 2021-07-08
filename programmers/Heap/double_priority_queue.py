import heapq


# "I 숫자": 큐에 주어진 숫자를 삽입
# "D 1": 큐에서 최대값 삭제
# "D -1": 큐에서 최소값 삭제

# 제한 사항
# - 최대값/최소값이 둘 이상인 경우 하나만 삭제
# - 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우 -> 해당 연산 무시

operations = ["I -45", "I 653", "D 1", "I -642",
              "I 45", "I 97", "D 1", "D -1", "I 333"]


def solution(operations):
    operations = [op.split(" ") for op in operations]
    # operations 마다 heap을 최대힙 또는 최소힙으로 변경
    heap = []
    onoff = True  # True 이면 최소힙, False이면 최대힙

    for op in operations:
        if op[0] == "I":
            if not onoff:  # 최대힙이라면 최소힙으로 변경
                heap = [(-1)*i for i in heap]
                heapq.heapify(heap)
                onoff = True
            heapq.heappush(heap, int(op[1]))
        elif op[0] == "D" and op[1] == "1" and len(heap) > 0:  # 최대값 pop
            if onoff:  # 최소힙이라면 최대힙으로 변경
                heap = [(-1)*i for i in heap]
                heapq.heapify(heap)
                onoff = False
            heapq.heappop(heap)
        elif op[0] == "D" and op[1] == "-1" and len(heap) > 0:  # 최소값 pop
            if not onoff:  # 최대힙이라면 최소힙으로 변경
                heap = [(-1)*i for i in heap]
                heapq.heapify(heap)
                onoff = True
            heapq.heappop(heap)
        print("heap: ", heap)

    if len(heap) == 0:
        return [0, 0]
    else:
        min = 0
        max = 0
        if onoff:
            min = heap[0]
            heap = [(-1)*i for i in heap]
            heapq.heapify(heap)
            max = (-1) * heapq.heappop(heap)

        else:
            max = (-1) * heap[0]
            heap = [(-1)*i for i in heap]
            heapq.heapify(heap)
            min = heap[0]
        return [max, min]


print(solution(operations))
