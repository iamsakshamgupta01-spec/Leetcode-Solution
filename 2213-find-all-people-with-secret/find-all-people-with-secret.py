class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        # Person 0 shares secret with firstPerson at time 0
        union(0, firstPerson)
        
        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])
        
        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            people = []
            
            # Process all meetings at same time
            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                union(x, y)
                people.append(x)
                people.append(y)
                i += 1
            
            # Reset people not connected to 0
            for p in people:
                if find(p) != find(0):
                    parent[p] = p
        
        # Collect result
        root0 = find(0)
        return [i for i in range(n) if find(i) == root0]
