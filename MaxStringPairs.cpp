class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        int count = 0;
        for (int i = 0; i < words.size(); i++) {
            for (int j = 0; j < words.size(); j++) {
                string rev = words[j];
                reverse(words[j].begin(), words[j].end());
                if (i != j && words[i] == rev) {
                    count++;
                }
            }
        }
        return count;
    }
};
