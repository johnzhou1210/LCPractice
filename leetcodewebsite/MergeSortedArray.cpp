class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        
        // append nums2 to nums1
        for (int i = 0; i < n; i++) {
            nums1[m+i] += nums2[i];
        }

        int start_indx = m;
        int end_indx = m+n-1;

        while (start_indx <= end_indx) {
            for (int i = start_indx; i > 0; i--) {
                if (nums1[i] < nums1[i-1]) {
                    swap(nums1[i], nums1[i-1]);
                }
            }
            start_indx++;
        }

    }
};
