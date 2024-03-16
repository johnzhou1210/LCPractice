class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (i != j && nums[i] + nums[j] == target) {
                    return {i,j};
                }
            }
        }
        return {0,0};
    }

    vector<int> twoSum2(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            map[nums[i]] = i;
        }

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (map.count(complement) && map[complement] != i) {
                return {i, map[complement]};
            }
        }
        return {};
    }   


};
