class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& A) {
        vector<bool> ans;
        int num = 0;

        for (int bit : A) {
            num = (num * 2 + bit) % 5;
            ans.push_back(num == 0);
        }

        return ans;
    }
};
