class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        // create a set to keep track of what is unique
        unordered_set<string> set;
        // end current string check when you reach @
        for (int i = 0; i < emails.size(); i++) {
            string address = "";
            bool ignore_chars = false;
            for (int j = 0; j < emails[i].length(); j++) {
                if (!ignore_chars && isalpha(emails[i][j])) {
                    address += emails[i][j];
                } else if (emails[i][j] == '+') {
                    // ignore all characters until reached @
                    ignore_chars = true;
                } else if (emails[i][j] == '@') {
                    // append the rest of the string onto address.
                    address += emails[i].substr(j);
                    break;
                }
            }
            // add address to set
            set.insert(address);
        }
        return set.size();
    }
};
