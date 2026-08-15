class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre) 
        

        visited = set()
        def dfs(crs):
            if pre_map[crs] == []:
                return True 
            
            if crs in visited:
                return False 
            
            visited.add(crs)
            for course in pre_map[crs]:
                if not dfs(course): return False 
            
            pre_map[crs] = []
            visited.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False 
        
        return True