class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        from collections import defaultdict
        rows = defaultdict(list)
        cols = defaultdict(list)

        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)

        for k in rows:
            rows[k].sort()
        for k in cols:
            cols[k].sort()

        ans = 0
        for x, y in buildings:
            row_list = rows[x]
            col_list = cols[y]
            # Check left & right
            if row_list[0] < y < row_list[-1]:
                # Check above & below
                if col_list[0] < x < col_list[-1]:
                    ans += 1
        return ans
