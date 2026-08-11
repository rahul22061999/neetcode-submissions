class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [-num for num in nums]
        heapq.heapify(minheap)
        res = []
        while k > 0:
            num = heapq.heappop(minheap)
            res.append(num)
            k-=1

            if  k ==0 :
                return -res[-1]
            


