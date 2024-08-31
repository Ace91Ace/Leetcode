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
        vector <int> ll;
        ListNode* curr = head;

        while (curr != nullptr){
            ll.push_back(curr->val);
            curr = curr->next;
        }

        int sum = 0;

        int n = ll.size()-1;
        for (int i = n ; i >= 0 ;i--){
            sum += ll[i] * pow(2,n-i);
        }

        return sum;
    }
};