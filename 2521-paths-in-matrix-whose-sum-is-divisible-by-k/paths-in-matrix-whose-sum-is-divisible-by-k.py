class Solution:
    def numberOfPaths(self, grid, k):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[0] * k for _ in range(n)]
        
        for i in range(m):
            new_dp = [[0] * k for _ in range(n)]
            for j in range(n):
                val = grid[i][j] % k
                if i == 0 and j == 0:
                    new_dp[0][val] = 1
                else:
                    for r in range(k):
                        if i > 0:
                            nr = (r + val) % k
                            new_dp[j][nr] = (new_dp[j][nr] + dp[j][r]) % MOD
                        if j > 0:
                            nr = (r + val) % k
                            new_dp[j][nr] = (new_dp[j][nr] + new_dp[j-1][r]) % MOD
            dp = new_dp

        return dp[n-1][0]
