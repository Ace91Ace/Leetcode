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
        if (head == nullptr) {  
            return false; // If the list is empty, return false  
        }  
        
        ListNode* tx = head;          // Pointer moving one step  
        ListNode* ox = head;          // Pointer moving two steps  

        while (ox != nullptr && ox->next != nullptr) { // Check if ox and ox->next are valid  
            tx = tx->next;            // Move tx one step  
            ox = ox->next->next;      // Move ox two steps  

            if (tx == ox) {           // Check if they meet  
                return true;          // Cycle detected  
            }  
        }  
        return false;                 // No cycle  
    }  
};