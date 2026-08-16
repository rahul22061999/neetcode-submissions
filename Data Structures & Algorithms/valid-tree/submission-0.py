class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj_list = {i:[] for i in range(n)}
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)
        
        visited = set()

        def dfs(node, parent):
            if  node in visited:
                return False
            
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue 
                
                if not dfs(neighbour, node):
                    return False 
            
            return True 
        

        return dfs(0, -1) and len(visited) == n 