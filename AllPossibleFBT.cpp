/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> allPossibleFBT(int n) {
        if (n == 1) {
            return {new TreeNode()};
        }
        // impossible if n is even
        if (n % 2 == 0) {
            return {};
        }
        
        vector<TreeNode*> result;
        for (int curr_left_node = 1; curr_left_node < n; curr_left_node += 2) {
            int curr_right_node = n - 1 - curr_left_node;
            vector<TreeNode*> curr_left_subtrees = allPossibleFBT(curr_left_node);
            vector<TreeNode*> curr_right_subtrees = allPossibleFBT(curr_right_node);

            for (TreeNode* curr_left_tree : curr_left_subtrees) {
                for (TreeNode* curr_right_tree : curr_right_subtrees) {
                    TreeNode* curr_root = new TreeNode(0);
                    curr_root->left = curr_left_tree;
                    curr_root->right = curr_right_tree;
                    result.push_back(curr_root);
                }
            }

        }

        return result;
    }
};
