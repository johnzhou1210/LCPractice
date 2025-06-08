class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        // we only need to use the one word from words as a basis for comparison
        unordered_map<char, int> freqs;
        for (char ch : words[0]) {
            if (freqs.find(ch) == freqs.end()) {
                freqs[ch] = 1;
            } else {
                freqs[ch]++;
            }
        }

        vector<string> result;

        for (const auto& pair : freqs) {
            int lowest_frequency_of_current_char = pair.second;
            for (int i = 1; i < words.size(); i++) {
                int frequency_of_current_char = 0;
                for (char ch : words[i]) {
                    if (ch == pair.first) {
                        frequency_of_current_char++;
                    }
                }
                if (frequency_of_current_char < lowest_frequency_of_current_char) {
                    lowest_frequency_of_current_char = frequency_of_current_char;
                }
            }
            if (lowest_frequency_of_current_char > 0) {
                // current char is a common char.
                for (int i = 0; i < lowest_frequency_of_current_char; i++) {
                    result.push_back(string(1, pair.first));
                }
                
            }
        }
        return result;
    }
};
