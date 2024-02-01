class Solution {
public:

    int charFrequency(string str, char match) {
        int freq = 0;
        for (char ch : str) {
            if (ch == match) {
                freq++;
            }
        }
        return freq;
    }

    bool wordIsCompleting(unordered_map<char, int>& map, string word) { 
        // return how much frequency there is. If less than plate, return unreachable number.
        int frequency_sum = 0;
        for (const auto& pair : map) {
            if (charFrequency(word, pair.first) < pair.second) {
                return false;
            }
        }
        return true;
    }

    string shortestCompletingWord(string licensePlate, vector<string>& words) {
        // first get rid of unwanted spaces and numbers and turn everything to lowercase
        // "ls3 4w6" => "sw"
        //  ["looks","pest","stew","show"]
        string cleaned_plate = "";
        for (int i = 0; i < licensePlate.length(); i++) {
            if (isalpha(licensePlate[i])) {
                cleaned_plate += tolower(licensePlate[i]);
            }
        }

        // do a character bag of words on the plate
        unordered_map<char, int> map;
        for (char ch : cleaned_plate) {
            if (map.find(ch) == map.end()) {
                map[ch] = 1;
            } else {
                map[ch] += 1;
            }
        }

        // find word in words that contains an equal or greater amount of the same letters in the cleaned plate.
        // ["looks","pest","stew","show"] => ["stew", "show"]
        vector<string> completing_words;
        
        for (string word : words) {
            if (wordIsCompleting(map, word)) {
                completing_words.push_back(word);
            }
        }

        // find the integer of shortest length
        int shortest_length = 16;

        for (string str : completing_words) {
            if (str.length() < shortest_length) {
                shortest_length = str.length();
            }
        }

        // iterate and stop when the current word is of that shortest length and return.

        for (int i = 0; i < completing_words.size(); i++) {
            if (completing_words[i].length() == shortest_length) {
                return completing_words[i];
            }
        }
        return completing_words[completing_words.size() - 1];
    }
};
