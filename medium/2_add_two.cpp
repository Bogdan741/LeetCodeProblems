#include <cmath>
struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    // They expect other solution as list can hold varialble length integer
    ListNode* addTwoNumbersBad(ListNode* l1, ListNode* l2) {
        int counter1{1};
        int sum1{0};
        ListNode* first = l1;
        // Get the first value
        while(first->next != nullptr){
            sum1+=first->val*counter1;
            counter1*=10;
            first = first->next;
        }
        sum1+=first->val*counter1;

        int counter2{1};
        int sum2{};
        ListNode* second = l2;

        // Get the second value
        while(second->next != nullptr){
            sum2+=second->val * counter2;
            counter2*=10;
            second = second->next;
        }
        sum2+=second->val*counter2;
        
        int res = sum1 + sum2;

        // Put the res to the list
        ListNode* new_list = nullptr;
        ListNode* cur_node = new_list;
        while(res!=0){
            int digit = res%10;
            res/=10;

            ListNode* next_node = new ListNode();
            next_node->val = digit;
            if(cur_node == nullptr){
                cur_node = next_node;
            }
            else{
                cur_node->next = next_node;
                cur_node = next_node;
            }
        }
        return new_list;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int overflow{0};
        ListNode* res{};
        ListNode* next{res};
        ListNode* firstList = l1;
        ListNode* secondList = l2;
        // List intersection
        while(firstList && secondList){
            int num = firstList->val + secondList->val + overflow;
            overflow = num / 10;
            if(res){
                ListNode * node = new ListNode;
                node->val = num % 10;
                next->next = node;
                next = node;
            }
            else{
                res = new ListNode;
                next = res;
                res->val = num % 10;
            }
            firstList = firstList->next;
            secondList = secondList->next;
        }
        // If firstList bigger than secondList
        while(firstList){
            int num = firstList->val + overflow;
            overflow = num / 10;
            if(res){
                ListNode * node = new ListNode;
                node->val = num % 10;
                next->next = node;
                next = node;
            }
            else{
                res = new ListNode;
                next = res;
                res->val = num % 10;
            }
            firstList = firstList->next;
        }
        // If secondList bigger than firstList
        while(secondList){
            int num = secondList->val + overflow;
            overflow = num / 10;
            if(res){
                ListNode * node = new ListNode;
                node->val = num % 10;
                next->next = node;
                next = node;
            }
            else{
                res = new ListNode;
                next = res;
                res->val = num % 10;
            }
            secondList = secondList->next;
        }

        if(overflow){
            ListNode * node = new ListNode;
            node->val = overflow;
            next->next = node;
        }
        return res;
    }
};
