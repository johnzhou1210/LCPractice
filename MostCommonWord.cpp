class Solution {
public:

    string cleanString(string paragraph) {
        string bad_symbols = "!?',;.";
        string result;
        for (char ch : paragraph) {
            if (bad_symbols.find(ch) == string::npos) {
                result += tolower(ch);
            } else {
                result += ' ';
            }
        }
        return result;
    }

    string mostCommonWord(string paragraph, vector<string>& banned) {
        // create banned word set for quick access
        unordered_set<string> set;
        for (string word : banned) {
            set.insert(word);
        }
        unordered_map<string, int> unbanned_words;

        // turn string to lowercase and get rid of punctuation
        string str = cleanString(paragraph);
        string curr_word = "";
        for (int i = 0; i < str.length(); i++) {
            if (str[i] != ' ') {
                curr_word += str[i];
            } else {
                // check if current word is not a banned word
                if (curr_word != "" && set.find(curr_word) == set.end()) {
                    // add to unbanned_words
                    if (unbanned_words.find(curr_word) ==
                        unbanned_words.end()) {
                        unbanned_words[curr_word] = 1;
                    } else {
                        unbanned_words[curr_word]++;
                    }
                }
                // reset curr_word
                curr_word = "";
            }
        }
        if (curr_word != "") {
            // check if current word is not a banned word
            if (curr_word != "" && set.find(curr_word) == set.end()) {
                // add to unbanned_words
                if (unbanned_words.find(curr_word) == unbanned_words.end()) {
                    unbanned_words[curr_word] = 1;
                } else {
                    unbanned_words[curr_word]++;
                }
            }
            // reset curr_word
            curr_word = "";
        }

        // go through unbanned words and pick the one with the highest frequency
        string highest_frequency_word = "";
        int highest_frequency = 0;
        for (const auto& pair : unbanned_words) {
            if (pair.second > highest_frequency) {
                highest_frequency = pair.second;
                highest_frequency_word = pair.first;
            }
        }
        return highest_frequency_word;
    }

};
