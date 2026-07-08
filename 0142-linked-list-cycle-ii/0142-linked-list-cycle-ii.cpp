/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while(fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast){
                break;
            }
            
        }
        if(fast == nullptr || fast->next == nullptr){
            return nullptr;
        }

        ListNode* p1 = head;
        while(p1 != nullptr){
            if(p1 == slow){
                return p1;
            }
            p1 = p1->next;
            slow = slow->next;
        }
        return nullptr;
    }
};