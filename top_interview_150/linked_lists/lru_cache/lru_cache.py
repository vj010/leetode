from typing import Optional, Dict


class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.next: Optional[Node] = None
        self.parent: Optional[Node] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head: Node = Node(-1, -1)
        self.tail: Node = self.head
        self.size = 0
        self.key_map: Dict[int, Node] = {}
        pass

    def get(self, key: int) -> int:
        if key in self.key_map:
            self.__update_access_list(key)
            return self.key_map[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            self.key_map[key].val = value
            self.__update_access_list(key)
            return

        if self.size < self.capacity:
            print("here")
            new_node = Node(key, value)
            self.key_map[key] = new_node
            self.tail.next = new_node
            new_node.parent = self.tail
            self.tail = self.tail.next
            self.tail.next = None
            self.size += 1
            return

        new_node = Node(key, value)
        self.key_map[key] = new_node
        lru_node = self.head.next

        if lru_node is not None:
            if lru_node == self.tail:
                self.key_map.pop(lru_node.key, None)
                lru_node.val = value
                lru_node.key = key
                return
            self.head.next = lru_node.next
            if lru_node.next is not None:
                lru_node.next.parent = self.head
            self.key_map.pop(lru_node.key, None)  # type: ignore
        self.tail.next = new_node
        new_node.parent = self.tail
        self.tail = self.tail.next
        self.tail.next = None
        # self.size += 1

    def __update_access_list(self, key: int):
        node: Node = self.key_map[key]
        # print(f"node:{node.key}")
        # print(f"node next:{node.next.key}")  # type: ignore
        # print(f"tail:{self.tail.key}")
        self.tail.next = node
        parent_node: Optional[Node] = node.parent
        node.parent = self.tail
        if parent_node is None:
            return
        # print(f"parent:{parent_node.key}")
        parent_node.next = node.next
        if node.next is not None:
            node.next.parent = parent_node
        # print(f"parent next:{parent_node.next.next.key}")  # type: ignore
        self.tail = self.tail.next
        self.tail.next = None

    def printKey(self):
        current_root: Optional[Node] = self.head.next
        # print(f"current_root:{current_root.key}")  # type: ignore
        while current_root is not None:
            print(f"({current_root.key}, {current_root.parent.key})", end=" ")  # type: ignore
            current_root = current_root.next
        print("\n")
        # print(f"currentK Keys:{self.key_map.keys()}")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(5)
# # param_1 = obj.get(key)
# obj.put(1, 2)
# obj.put(2, 7)
# obj.put(3, 99)
# obj.put(4, 90)
# obj.put(5, 69)
# obj.put(6, 70)
# obj.put(7, 70)
# obj.printKey()
# print(obj.get(1))
# obj.printKey()
# print(obj.get(2))
# obj.printKey()
# print(obj.get(4))
# obj.put(8, 81)
# obj.printKey()

operations = [
    "LRUCache",
    "get",
    "get",
    "put",
    "get",
    "put",
    "put",
    "put",
    "put",
    "get",
    "put",
]

operands = [
    [1],
    [6],
    [8],
    [12, 1],
    [2],
    [15, 11],
    [5, 2],
    [1, 15],
    [4, 2],
    [5],
    [15, 15],
]
# obj.printKey()
obj = None
for i in range(len(operations)):
    if operations[i] == "LRUCache":
        obj = LRUCache(operands[i][0])

    if operations[i] == "put":
        if obj is not None:
            obj.put(operands[i][0], operands[i][1])
            # obj.printKey()

    if operations[i] == "get":
        if obj is not None:
            print(f"get val : {operands[i][0]} -> {obj.get(operands[i][0])}")
            # obj.printKey()
