class Solution {
public:

    int modConvertToBinary(int n) {
        if (n == 0) {
            return 0;
        }
        int binary_num = 0;
        long long digit_place = 1;
        int ones = 0;
        while (n > 0) {
            int remainder = n % 2;
            if (remainder == 1) {
                ones++;
            }
            binary_num = binary_num + (remainder * digit_place);
            n = n / 2;
            digit_place = digit_place * 10;
        }
        return ones;
    }

    vector<int> countBits(int n) {
        // generate array from 0 to n filled with binary conversions
        vector<int> conversions(n+1, 0);
        for (int i = 0; i <= n; i++) {
            conversions[i] = modConvertToBinary(i);
        }
        return conversions;
    }
};
