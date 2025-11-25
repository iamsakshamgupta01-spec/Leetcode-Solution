class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        # If K has factor 2 or 5, no repunit possible
        if K % 2 == 0 or K % 5 == 0:
            return -1
        
        rem = 0
        for n in range(1, K + 1):
            rem = (rem * 10 + 1) % K
            if rem == 0:
                return n
        
        return -1
