class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        // First reduce both lists to a single unordered map
        // list1 = ["happy","sad","good", "depressed"], list2 = ["sad","happy","good","crazy"]
        
        unordered_map<string, int> map;
        for (int i = 0; i < list1.size(); i++) {
            if (find(list2.begin(), list2.end(), list1[i]) != list2.end()) {
                map[list1[i]] = i;
            }
        }
         // map = [ "happy":0, "sad":1, "good":2 ]

        for (int i = 0; i < list2.size(); i++) {
            if (find(list1.begin(), list1.end(), list2[i]) != list1.end()) {
                map[list2[i]] += i;
            }

        }
         // map = [ "happy":0+1, "sad":1+0, "good":2+2 ]

        // Then go through all the elements of the unordered map and find the lowest sum.

        int lowest_sum = 2002;
        for (const auto& pair : map) {
            if (pair.second >=0 && pair.second < lowest_sum) {
                lowest_sum = pair.second;
            }
        }

        // Then go through the map again and push back to the results array all words of the lowest sum value.
        vector<string> result;
        for (const auto& pair : map) {
            if (pair.second == lowest_sum) {
                result.push_back(pair.first);
            }
        }

        return result;

    }
};
