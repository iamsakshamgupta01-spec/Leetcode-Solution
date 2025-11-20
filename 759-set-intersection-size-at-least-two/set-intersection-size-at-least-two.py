class Solution:
    def intersectionSizeTwo(self, intervals):
        # Sort by end asc, start desc
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        S = []
        p1, p2 = -1, -1  # last two chosen points
        
        for start, end in intervals:
            # Case 1: interval contains both
            if start <= p1:
                continue
            # Case 2: interval contains one (p2 only)
            if start <= p2:
                p1 = p2
                p2 = end
                S.append(end)
            else:
                # Case 3: contains zero — add two points
                p1 = end - 1
                p2 = end
                S.append(end - 1)
                S.append(end)
        
        return len(S)
