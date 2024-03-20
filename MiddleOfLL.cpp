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
    ListNode* middleNode(ListNode* head) {
        // determine size first
        int size = 0;
        ListNode* curr_node = head;
        while (curr_node != nullptr) {
            size++;
            curr_node = curr_node->next;
        }
        int stop_point = (size / 2) + 1;
        for (int i = 0; i < stop_point - 1; ++i) {
            head = head->next;
        }
        return head;
    }


    ListNode* middleNode2(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return fast->next == nullptr ? slow : slow->next; 
    }

};
