#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode* createList (vector<int> arr) {
    if (arr.begin() == arr.end()) {
        return nullptr;
    }
    ListNode *head, *p;
    p = new ListNode(*arr.begin());
    head = new ListNode(-1);
    head->next = p;

    auto it = arr.begin() + 1;
    while (it != arr.end()) {
        p->next = new ListNode(*it++);
        p = p->next;
    }
    return head;
}

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *beforeHead = new ListNode(0); 
        beforeHead->next = head;
        ListNode *p = beforeHead, *q = beforeHead;
        while (n > 0) {
            q = q->next;
            --n;
        }
        
        while (q->next != nullptr) {
            p = p->next;
            q = q->next;
        }

        p->next = p->next->next;
        return beforeHead->next;
    }
};


int main () {
    vector<int> arr {1, 2, 3, 4, 5};
    // vector<int> arr {1};

    for (int i = 1; i <= arr.size(); i++) {
        ListNode *head = createList(arr);

        Solution s;
        s.removeNthFromEnd(head, i);
        head = head->next;
        while (head != nullptr) {
            cout << head->val << " ";
            head = head->next;
        }
        cout << endl;
    }

    return 0;
}
