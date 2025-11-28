class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k):
        from collections import defaultdict, deque
        
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # To avoid revisiting nodes
        visited = set()
        count = 0   # count of components divisible by k

        def dfs(node):
            nonlocal count
            visited.add(node)
            
            total_sum = values[node]
            
            for nei in graph[node]:
                if nei not in visited:
                    child_sum = dfs(nei)
                    
                    # If child component sum is divisible by k → form new component
                    if child_sum % k == 0:
                        count += 1
                    else:
                        total_sum += child_sum
                    
            return total_sum
        
        # DFS from root (0)
        root_sum = dfs(0)
        
        # If root component also divisible by k
        if root_sum % k == 0:
            count += 1
        
        return count
