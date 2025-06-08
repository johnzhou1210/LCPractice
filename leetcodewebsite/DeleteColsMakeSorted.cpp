class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int cols_to_delete = 0;
        int curr_col = 0;
        while (curr_col < strs[0].length()) {
            int curr_row = 0;
            while (curr_row < strs.size() - 1) {
                if (strs[curr_row][curr_col] > strs[curr_row + 1][curr_col]) {
                    cols_to_delete++;
                    break;
                }
                curr_row++;
            }
            curr_col++;
        }
        return cols_to_delete;
    }
};
