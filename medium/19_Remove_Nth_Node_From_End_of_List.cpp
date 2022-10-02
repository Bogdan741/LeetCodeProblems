
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    // Naive approuch
    ListNode* removeNthFromEndNaive(ListNode* head, int n) {
        int length = 0;
        ListNode* tmp = head;
        while(tmp){
            tmp = tmp->next;
            ++length;
        }
        ListNode* cur = head;
        ListNode* prev = nullptr;
        int i = length - n;
        while(i-- && cur->next != nullptr){
            prev = cur;
            cur = cur->next;
        }
        if(prev == nullptr)
            return cur->next;
        prev->next = cur->next;
        return head;
    }

    // Solution
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* first = head;
        ListNode* second = head;
        while(n-- && second->next)
            second=second->next;
        if(second->next==nullptr && n >= 0)
            return first->next;
        while(second->next != nullptr){
            first = first->next;
            second = second->next;
        }
        first->next = first->next->next;
        return head;
    }
};
