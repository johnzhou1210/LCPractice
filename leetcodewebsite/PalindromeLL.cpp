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

    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr_node = head;
        
        while (curr_node != nullptr) {
            ListNode* next_node = curr_node->next;
            curr_node->next = prev;
            prev = curr_node;
            curr_node = next_node;
        }

        return prev;
    }


    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast->next!=nullptr && fast->next->next!= nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        slow->next = reverseList(slow->next);

        ListNode* p1 = head;
        ListNode* p2 = slow->next;
        while (p2 != nullptr) {
            if (p1->val != p2->val) {
                return false;
            }
            p1 = p1->next;
            p2 = p2->next;
        }
        return true;
    }
};
