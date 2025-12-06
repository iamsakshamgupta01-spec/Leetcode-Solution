#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1e9 + 7;

    int countPartitions(vector<int>& nums, int k) {
        int n = nums.size();

        vector<long long> dp(n + 1, 0), pref(n + 1, 0);
        dp[0] = 1;
        pref[0] = 1;

        deque<int> dqMax, dqMin;
        int left = 0;

        for (int right = 0; right < n; right++) {

            // Maintain decreasing queue for max
            while (!dqMax.empty() && nums[dqMax.back()] <= nums[right])
                dqMax.pop_back();
            dqMax.push_back(right);

            // Maintain increasing queue for min
            while (!dqMin.empty() && nums[dqMin.back()] >= nums[right])
                dqMin.pop_back();
            dqMin.push_back(right);

            // Shrink window while invalid
            while (!dqMax.empty() && !dqMin.empty() &&
                   nums[dqMax.front()] - nums[dqMin.front()] > k) {

                if (dqMax.front() == left) dqMax.pop_front();
                if (dqMin.front() == left) dqMin.pop_front();
                left++;
            }

            // dp[right+1] = sum(dp[left] .. dp[right])
            long long ways = pref[right];
            if (left > 0) ways = (ways - pref[left - 1] + MOD) % MOD;

            dp[right + 1] = ways;
            pref[right + 1] = (pref[right] + dp[right + 1]) % MOD;
        }

        return dp[n];
    }
};
