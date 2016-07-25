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
    return head->next;
}

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) {
            return nullptr;
        }

        while (lists.size() > 1) {
            lists.push_back(mergeTwoLists(lists[0], lists[1]));
            lists.erase(lists.begin());
            lists.erase(lists.begin());
        }

        return lists[0];
    }
private:
    ListNode* mergeTwoLists(ListNode *l1, ListNode *l2) {
        if (l1 == nullptr) {
            return l2;
        }
        if (l2 == nullptr) {
            return l1;
        }

        if (l1->val < l2->val) {
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        } else {
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    }
};


int main () {
    vector<int> v1 {1,4,7},
                v2 {2,5,8},
                v3 {3,6,9};
    ListNode *l1 = createList(v1),
             *l2 = createList(v2),
             *l3 = createList(v3);
    vector<ListNode*> lists {l1, l2, l3};

    Solution s;
    ListNode *h = s.mergeKLists(lists);
    while (h != nullptr) {
        cout << h->val << " ";
        h = h->next;
    }
    cout << endl;

    return 0;
}
