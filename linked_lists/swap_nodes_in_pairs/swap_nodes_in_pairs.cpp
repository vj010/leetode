#include <bits/stdc++.h>

//  Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *swapPairs(ListNode *head)
    {
        ListNode *root = head;
        if (head == nullptr)
        {
            return nullptr;
        }
        ListNode *prevRoot = nullptr;
        while (root != nullptr)
        {
            std::cout << root->val << std::endl;
            // std::cout << root->next->val << std::endl;

            ListNode *child = root->next;
            if (child != nullptr)
            {
                root->next = child->next;
                child->next = root;
                if (root == head)
                {
                    head = child;
                }
                if (prevRoot != nullptr)
                {
                    prevRoot->next = child;
                }

                prevRoot = root;
            }
            root = root->next;
        }

        return head;
    }
};

int main(int argc, char *argv[])
{
    ListNode *root;
    ListNode *head = new ListNode(1);
    root = head;
    head->next = new ListNode(2);
    head = head->next;
    head->next = new ListNode(3);
    head = head->next;
    head->next = new ListNode(4);
    head = head->next;
    head->next = new ListNode(5);

    Solution sol;
    root = sol.swapPairs(nullptr);

    while (root != nullptr)
    {
        std::cout << root->val << " ";
        root = root->next;
    }

    return 0;
}
