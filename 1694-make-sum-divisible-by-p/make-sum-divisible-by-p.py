class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums)
        rem = total % p
        if rem == 0:
            return 0

        prefix = 0
        seen = {0: -1}  # prefix mod → index
        ans = len(nums)

        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            needed = (prefix - rem) % p

            if needed in seen:
                ans = min(ans, i - seen[needed])

            seen[prefix] = i

        return ans if ans < len(nums) else -1
