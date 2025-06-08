class Solution {
public:


    bool canBuild(unordered_map<char,int>& str_map, unordered_map<char,int>& avail_map) {
        for (const auto& pair : str_map) {
            if (avail_map.find(pair.first) == avail_map.end() || pair.second > avail_map[pair.first]) {
                return false;
            }
        }
        return true;
    }

    int countCharacters(vector<string>& words, string chars) {
        unordered_map<char, int> available_chars;
        for (char ch : chars) {
            if (available_chars.find(ch) == available_chars.end()) {
                available_chars[ch] = 1;
            } else {
                available_chars[ch]++;
            }
        }

        int result = 0;

        for (int i = 0; i < words.size(); i++) {
            // count number of characters in current word
            unordered_map<char, int> char_map;
            for (char ch : words[i]) {
                if (char_map.find(ch) == available_chars.end()) {
                    char_map[ch] = 1;
                } else {
                    char_map[ch]++;
                }
            }
            // in order for word to be buildable, every key value in char_map must be less than its corresponding key value in available_chars.
            if (canBuild(char_map, available_chars)) {
                result += words[i].length();
            }

        }
        return result;
    }
};
