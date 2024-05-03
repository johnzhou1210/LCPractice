class Solution {
public:
    void reverseString(vector<char>& s) {
        int ptr_1 = 0, ptr_2 = s.size()-1;
        while (ptr_1 < ptr_2 && ptr_1 != ptr_2) {
            swap(s[ptr_1], s[ptr_2]);
            ptr_1++;
            ptr_2--;
        }
    }
};
