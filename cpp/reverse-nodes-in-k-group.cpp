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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == nullptr || k == 1) {
            return head;
        }

        int num = 0;

        ListNode *preHead = new ListNode(0);
        preHead->next = head;
        ListNode *cur = preHead->next, *next, *pre = preHead;

        while (cur != nullptr) {
            cur = cur->next;
            ++num;
        }

        while (num >= k) {
            cur = pre->next;
            next = cur->next;
            for (int i = 1; i < k; i++) {
                cur->next = next->next;
                next->next = pre->next;
                pre->next = next;
                next = cur->next;
            }
            pre = cur;
            num -= k;
        }

        return preHead->next;
    }
};

int main () {
    vector<int> v {1,2,3,4,5,6,7,8,9};
    ListNode *head = createList(v);

    Solution s;
    head = s.reverseKGroup(head, 6);
    cout << head->val << endl;
    while (head != nullptr) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;

    return 0;
}
