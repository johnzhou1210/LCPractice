class Solution {
public:
    unordered_map<int,vector<int>> memo;

    vector<int> generateRow(int rowNum) { // rowNum is the source/previous row
        vector<int> result(rowNum + 1, 1);
        for (int i = 0; i < memo[rowNum].size() - 1; i++) {
            result[i + 1] = memo[rowNum][i] + memo[rowNum][i+1];
        }
        return result;
    }

    vector<vector<int>> generate(int numRows) {
        memo[1] = {1}; memo[2] = {1,1};
        vector<vector<int>> result;
        for (int i = 1; i <= numRows; i++) {
            if (memo.find(i) == memo.end()) {
                memo[i] = generateRow(i-1);
            }
            result.push_back(memo[i]);
        }
        return result;
    }
};
