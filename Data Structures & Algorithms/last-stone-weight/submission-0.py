class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stone = [-stone for stone in stones]
        heapq.heapify(stone)

        while len(stone) > 1:
            first = heapq.heappop(stone)
            second = heapq.heappop(stone)

            if first !=second:
                heapq.heappush(stone, -abs(first - second))

        return -stone[0] if stone else 0