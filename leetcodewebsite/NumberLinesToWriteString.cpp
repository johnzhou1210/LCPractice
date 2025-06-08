class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        // build width dictionary
        unordered_map<char, int> map;
        for (char ch : s) {
            if (map.find(ch) == map.end()) {
                map[ch] = widths[ch - 97]; // a is 97 in ascii
            }
        }

        // keep track of how much lines used
        int lines_used = 1;
        // keep track of how much characters on current line
        int curr_line_num_chars = 0;
        // iterate through each character in s
        for (int i = 0; i < s.length(); i++) {
            int value_to_add = map[s[i]];
            if (curr_line_num_chars + value_to_add > 100) { // if current character overflows line, make a new line and add that character there.
                lines_used++;
                curr_line_num_chars = value_to_add;
            } else {
                curr_line_num_chars += value_to_add; // otherwise, add to current line.
            }

        }
        vector<int> result = {lines_used, curr_line_num_chars};
        return result;
    }
};
