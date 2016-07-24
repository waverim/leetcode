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
    head = new ListNode(0);
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr) {
            return l2;
        }
        ListNode *head = new ListNode(0), *p = l1, *q = l2;
        head->next = l1;
        if (l2 != nullptr && l1->val > l2->val) {
            head->next = l2;
            p = l2;
            q = l1;
        }
        ListNode *cur = p, *pn = p, *qn = q;

        while (cur != nullptr) {
            if (cur == p) {
                if (q == nullptr) {
                    break;
                } else if (p->next != nullptr && p->next->val < q->val) {
                    p = p->next;
                    cur = p;
                } else {
                    pn = p->next;
                    p->next = q;
                    p = pn;
                    cur = q;
                }
            } else if (cur == q) {
                if (p == nullptr) {
                    break;
                } else if (q->next != nullptr && q->next->val < p->val) {
                    q = q->next;
                    cur = q;
                } else {
                    qn = q->next;
                    q->next = p;
                    q = qn;
                    cur = p;
                }
            }
        }
        
        return head->next;
    }
};


int main () {
    vector<int> v1 {1},
                v2 {2,4,6,8,10,11,12};
    ListNode *l1 = createList(v1),
             *l2 = createList(v2);

    Solution s;
    ListNode *h = s.mergeTwoLists(l1->next, l2->next);
    while (h != nullptr) {
        cout << h->val << " ";
        h = h->next;
    }
    cout << endl;

    return 0;
}
