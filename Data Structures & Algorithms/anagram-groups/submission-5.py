class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for char in strs:
            sorted_char = ("".join(sorted(char)))

    
            group[sorted_char].append(char)
        

        return list(group.values())