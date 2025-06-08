class Solution {
public:
    int charSearch(string s, char c, int start, bool reverse) {
        if (!reverse) {
            for (int i = start; i < s.length(); i++) {
                if (s[i] == c) {
                    return i;
                }
            }
        } else {
            for (int i = start; i >= 0; i--) {
                if (s[i] == c) {
                    return i;
                }
            }
        }
        return -1;
    }

    vector<int> shortestToChar(string s, char c) {
        // iterate through s, cutting s off and finding the first occurence of
        // c. substring?
        vector<int> result;
        for (int i = 0; i < s.length(); i++) {
            int closest_right = (charSearch(s, c, i, false) != -1) ? charSearch(s, c, i, false) - i : pow(10, 4) + 1; 
            int closest_left = (charSearch(s, c, i, true) != -1) ? i - charSearch(s, c, i, true) : pow(10, 4) + 1;
            int smaller = (closest_right < closest_left) ? closest_right : closest_left;
            result.push_back(smaller);
        }
        return result;
    }
};
