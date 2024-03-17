class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        unordered_set<int> consistent;
        for (char ch : allowed) {
            consistent.insert(ch);
        }
        int count = 0;
        for (string str : words) {
            for (int i = 0; i < str.length(); i++) {
                if (consistent.find(str[i]) == consistent.end()) {
                    break;
                }
                if (i == str.length() - 1) {
                    count++;
                }
            }
        }
        return count;
    }
};
