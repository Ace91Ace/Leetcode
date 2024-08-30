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
    bool hasCycle(ListNode *head) {
        if(head == nullptr){
            return false;
        }
        ListNode* tx = head;
        ListNode* ox = head;

        while(tx != nullptr  && ox != nullptr && tx->next != nullptr){
            ox = ox->next; 
            tx = tx->next->next;

            if (tx == ox){
                return true;
            }
        }
        return false;
    }
};