import heapq
def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    priority_queue = []

    for i in range(len(enemy)):
        heapq.heappush(priority_queue, enemy[i])
        if len(priority_queue) > k:
            last = heapq.heappop(priority_queue)
            if last > n:
                return i
            n -= last
    return len(enemy)

solution(n=7,k=3,enemy=[1,2,4,2,4,5,3,3,1])