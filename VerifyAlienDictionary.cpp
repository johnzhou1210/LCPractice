class Solution {
public:

    bool isEarlierThan(string left, string right, unordered_map<char, int> dict) {
        if (left == right) {
            return true;
        }
        // iterate through the shorter string
        string longer = (left.length() >= right.length()) ? left : right;
        string shorter = (longer == left) ? right : left;
        for (int i = 0; i < shorter.length(); i++ ) {
            if ( dict[left[i]] < dict[right[i]] ) {
                return true;
            } else if (dict[left[i]] > dict[right[i]]) {
                return false;
            }
        }
        if (right.length() > left.length()) {
            return true;
        }
        return false;
    }

    bool isAlienSorted(vector<string>& words, string order) {
        unordered_map<char, int> dict;
        // populate alien dictionary
        for (int i = 0; i < order.length(); i++) {
            dict[order[i]] = i; 
        }

        for (int i = 0; i < words.size() - 1; i++) {
            if ( !isEarlierThan(words[i], words[i+1], dict) ) {
                return false;
            }
        }

        return true;

    }
};
