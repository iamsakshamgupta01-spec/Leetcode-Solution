class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0    # current streak of consecutive 1s
        result = 0
        
        for ch in s:
            if ch == '1':
                count += 1
                result = (result + count) % MOD
            else:
                count = 0
        
        return result
