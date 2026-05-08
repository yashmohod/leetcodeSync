class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        cooldown = deque()  # (-count, available_at_time)

        while maxHeap or cooldown:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1  # use one
                if cnt != 0:
                    cooldown.append((cnt, time + n))

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])

        return time



        
