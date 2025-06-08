class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        unordered_set<string> matches;
        for (int i = 0; i < words.size(); i++) {
            // words[i] is current word
            for (int j = 0; j < words.size(); j++) {
                if (words[i] != words[j] && words[j].find(words[i]) != string::npos) {
                    matches.insert(words[i]);
                }
            }
        }
        vector<string> result;
        for (const auto& elem : matches) {
            result.push_back(elem);
        }
        return result;
    }
};
