class Solution:
    def maxSumDivThree(self, nums):
        total = sum(nums)
        
        mod1 = []
        mod2 = []
        
        for x in nums:
            if x % 3 == 1:
                mod1.append(x)
            elif x % 3 == 2:
                mod2.append(x)
        
        mod1.sort()
        mod2.sort()
        
        if total % 3 == 0:
            return total
        
        ans = 0
        
        if total % 3 == 1:
            option1 = mod1[0] if len(mod1) >= 1 else float('inf')
            option2 = sum(mod2[:2]) if len(mod2) >= 2 else float('inf')
            ans = total - min(option1, option2)
        
        else:  # total % 3 == 2
            option1 = mod2[0] if len(mod2) >= 1 else float('inf')
            option2 = sum(mod1[:2]) if len(mod1) >= 2 else float('inf')
            ans = total - min(option1, option2)
        
        return ans
