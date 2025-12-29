from collections import defaultdict
from functools import lru_cache

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # Step 1: Build mapping
        mp = defaultdict(list)
        for a in allowed:
            mp[(a[0], a[1])].append(a[2])

        @lru_cache(None)
        def dfs(row: str) -> bool:
            # If only one block remains, pyramid is built
            if len(row) == 1:
                return True

            # Generate all possible next rows
            def build_next(i, curr):
                if i == len(row) - 1:
                    return dfs(curr)
                key = (row[i], row[i + 1])
                if key not in mp:
                    return False
                for ch in mp[key]:
                    if build_next(i + 1, curr + ch):
                        return True
                return False

            return build_next(0, "")

        return dfs(bottom)
