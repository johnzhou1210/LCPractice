class Solution {
public:
    vector<int> diStringMatch(string s) {
        // if first character is I: start at 0, else: start at s.length()
        vector<int> result;

        int next_increasing_number;
        int next_decreasing_number;
        if (s[0] == 'I') {
            result.push_back(0);
            next_increasing_number = result[0] + 1;
            next_decreasing_number = s.length();
        } else {
            result.push_back(s.length());
            next_increasing_number = 0;
            next_decreasing_number = result[0] - 1;
        }
        
        for (int i = 1; i < s.length(); i++) {
            if (s[i] == 'I') {
                result.push_back(next_increasing_number);
                next_increasing_number++;
            } else {
                result.push_back(next_decreasing_number);
                next_decreasing_number--;
            }
        }    

         if (s[s.length() - 1] == 'I') {
            result.push_back(next_increasing_number);
        } else {
            result.push_back(next_decreasing_number);
        }

        return result;
    }
};
