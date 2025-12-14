class Solution {
public:
    int numberOfWays(string corridor) {
        const int MOD = 1e9 + 7;
        long long ways = 1;
        int seats = 0;
        int plantsBetween = 0;
        bool countingPlants = false;

        for (char c : corridor) {
            if (c == 'S') {
                seats++;
                if (seats > 2 && seats % 2 == 1) {
                    ways = (ways * (plantsBetween + 1)) % MOD;
                }
                plantsBetween = 0;
                countingPlants = (seats % 2 == 0);
            } else if (c == 'P' && countingPlants) {
                plantsBetween++;
            }
        }

        return seats % 2 == 0 && seats > 0 ? ways : 0;
    }
};
