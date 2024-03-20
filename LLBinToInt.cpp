/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        // determine size of linked list
        int size = 0;
        ListNode* curr_node = head;
        while (curr_node != nullptr) {
            size++;
            curr_node = curr_node->next;
        }
        int result = 0;
        while (head != nullptr) {
            result += (pow(2, --size) * head->val);
            head = head->next;
        }
        return result;
    }
};
