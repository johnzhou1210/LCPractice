class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_map<string, string> map;
        for (vector<string> vec : paths) {
            map[vec[0]] = vec[1];
        }
        string curr_city = paths[0][0];
        string next_city = map[curr_city];
        while (map.count(next_city)) {
            next_city = map[next_city];
        }
        return next_city;
    }
};
