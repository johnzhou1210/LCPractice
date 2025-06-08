class Solution {
public:

    string& charBelongsToWhichRow(vector<string>& rows, char ch) {
        for (string& row : rows) {
            if (row.find(ch) != string::npos) {
                return row;
            }
        }
        static string none;
        return none;
    }

    vector<string> findWords(vector<string>& words) {
        vector<string> result;

        vector<string> rows =
        { "qwertyuiop",
          "asdfghjkl",
          "zxcvbnm" };

        for (int i = 0; i < words.size(); i++) {
            // for each word, take the first character and check which row it
            // belongs to. then the other characters in the word must also be in
            // that same row.
            char first_char;
            string* belongsToRow;
            for (int j = 0; j < words[i].length(); j++) {
                if (j == 0) {
                    first_char = tolower(words[i][j]);
                    belongsToRow = &charBelongsToWhichRow(rows, first_char);
                } else if ((*belongsToRow).find(tolower(words[i][j])) == string::npos) {
                    break;
                }
                if (j == words[i].length() - 1) {
                    result.push_back(words[i]);
                }
                
            }
        }
        return result;
    }

};
