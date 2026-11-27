class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        max_seq = 0 

        for n in values:

            if n - 1 not in values:
                longest = 1 

                while n + longest in values:
                    longest+=1 
                

                max_seq = max(max_seq, longest)
        
        return max_seq


            