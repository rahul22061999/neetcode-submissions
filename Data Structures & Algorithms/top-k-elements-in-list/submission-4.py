class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            counts[n] = counts.get(n, 0) +  1
        
        for i, j in counts.items():
            freq[j].append(i)
        
        final_count = [] 
        for j in range(len(freq) -1, 0, -1):
            for num in freq[j]:
                if len(final_count) >= k:
                    return final_count
                final_count.append(num)
        return final_count

