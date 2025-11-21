class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int n = s.size();
        vector<int> first(26, -1), last(26, -1);

        // Record first and last occurrence of each letter
        for (int i = 0; i < n; i++) {
            int c = s[i] - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }

        int result = 0;

        // For each character as the first and last character of palindrome
        for (int c = 0; c < 26; c++) {
            if (first[c] != -1 && last[c] != -1 && first[c] < last[c]) {
                unordered_set<char> middle;
                
                // Collect unique middle characters
                for (int i = first[c] + 1; i < last[c]; i++) {
                    middle.insert(s[i]);
                }

                result += middle.size();
            }
        }

        return result;
    }
};
