class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        minheap = [-count for count in counts.values()]
        heapq.heapify(minheap)

        q = deque()
        time = 0 

        while q or minheap:

            time +=1 

            if minheap:
                cnt = 1 + heapq.heappop(minheap)
                if cnt:
                    q.append([cnt , time + n])

            if q and q[0][1] == time:
                heapq.heappush(minheap, q.popleft()[0])
        
        return time


