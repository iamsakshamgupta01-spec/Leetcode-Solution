#include <bits/stdc++.h>
using namespace std;
static const long long MOD = 1000000007;

long long modFact(int n) {
    long long res = 1;
    for (int i = 2; i <= n; i++) {
        res = (res * i) % MOD;
    }
    return res;
}

class Solution {
public:
    int countPermutations(vector<int>& complexity) {
        int n = complexity.size();
        // The password for computer 0 is already decrypted,
        // so complexity[0] must be strictly less than every other complexity[i]
        for (int i = 1; i < n; i++) {
            if (complexity[0] >= complexity[i]) {
                return 0;
            }
        }
        // Otherwise, any permutation of the remaining (n-1) computers works
        return (int)modFact(n - 1);
    }
};
