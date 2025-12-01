class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        left, right = 0, sum(batteries) // n

        def can_run(t):
            total = 0
            for b in batteries:
                total += min(b, t)
            return total >= n * t

        while left < right:
            mid = (left + right + 1) // 2
            if can_run(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
