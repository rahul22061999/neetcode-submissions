class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        pre_map  = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        
        output = [] 
        visited = set()
        cycle = set()

        def dfs(crs):
            if crs in visited:
                return True
            
            if crs in cycle:
                return False 
            
            cycle.add(crs)

            for course in pre_map[crs]:
                if dfs(course) == False:
                    return False 
            
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True 
        

        for crs in range(numCourses):
            if dfs(crs) == False:
                return [] 
        
        return output
