#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode *head, *p;
        head = p = new ListNode(-1);
        while (l1 != nullptr || l2 != nullptr) {
            int val1 = l1 == nullptr ? 0 : l1->val;
            int val2 = l2 == nullptr ? 0 : l2->val;
            int sum = val1 + val2 + carry;
            p->next = new ListNode(sum % 10);
            carry = sum / 10;
            p = p->next;
            l1 = l1 == nullptr ? nullptr : l1->next;
            l2 = l2 == nullptr ? nullptr : l2->next;
        }
        if (carry > 0) {
            p->next = new ListNode(1);
        }
        return head->next;
    }
};

ListNode* createList (vector<int> arr) {
    if (arr.begin() == arr.end()) {
        return nullptr;
    }
    ListNode *head, *p;
    head = p = new ListNode(*arr.begin());
    
    auto it = arr.begin() + 1;
    while (it != arr.end()) {
        p->next = new ListNode(*it++);
        p = p->next;
    }
    return head;
}

int main () {
    vector<int> arr1{9};
    vector<int> arr2{9,9};
    
    ListNode *l1 = createList(arr1);
    ListNode *l2 = createList(arr2);

    Solution s;
    ListNode *result = s.addTwoNumbers(l1, l2);

    while (result != nullptr) {
        cout << result->val << " ";
        result = result->next;
    }
    cout << endl;
    
    return 0;
}
