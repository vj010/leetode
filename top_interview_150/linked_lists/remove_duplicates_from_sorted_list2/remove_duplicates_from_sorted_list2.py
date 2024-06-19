from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root: Optional[ListNode] = self.__getFirstUnique(head)
        current_node: Optional[ListNode] = root
        # print(f"root:{root.val}")  # type: ignore
        if root is not None:
            head = root.next
        else:
            head = None
        while head is not None and current_node is not None:
            current_node.next = self.__getFirstUnique(head)
            # print(f"current_node:{current_node.val}, head:{head.val}")
            current_node = current_node.next
            if current_node is not None:
                head = current_node.next
            else:
                head = None
        # print(f"exiting")
        return root

    def __getFirstUnique(self, head: Optional[ListNode]):
        if head is None:
            return None
        current = head
        head = head.next
        dup = False

        while head is not None:
            if head.val == current.val:
                dup = True
            else:
                if dup:
                    current = head
                    dup = False
                else:
                    break
            head = head.next

        if dup:
            return head
        else:
            return current

    def printList(self, head: Optional[ListNode]):
        while head is not None:
            print(head.val, end=" ")
            head = head.next
        print()


def getList(nums: List[int]) -> Optional[ListNode]:
    root: Optional[ListNode] = None
    current: Optional[ListNode] = None
    for i in nums:
        if root is None:
            root = ListNode(i)
            continue
        if current is None:
            current = root
        current.next = ListNode(i)
        current = current.next

    return root


list_root = getList([1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4])
sol = Solution()
new_root = sol.deleteDuplicates(list_root)
# print(f"new_root={new_root.val}")  # type: ignore
sol.printList(new_root)
