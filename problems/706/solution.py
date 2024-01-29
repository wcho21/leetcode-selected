# Accepted: 264ms (38.94%), 19.86MB (83.65%)

class Node:
    def __init__(self, key: int = 0, value: int = 0, nextNode: Optional[List] = None):
        self.key = key
        self.value = value
        self.next = nextNode

class MyHashMap:
    size = (2*11)-1

    def __init__(self):
        self.map: List[Node] = [Node() for _ in range(MyHashMap.size)]

    def _getHash(self, key: int):
        return key % MyHashMap.size

    def put(self, key: int, value: int) -> None:
        keyHash = self._getHash(key)
        node = self.map[keyHash]

        while node.next is not None:
            if key == node.next.key:
                node.next.value = value
                return

            node = node.next

        node.next = Node(key, value)

    def get(self, key: int) -> int:
        keyHash = self._getHash(key)
        node = self.map[keyHash]

        while node.next is not None:
            if key == node.next.key:
                return node.next.value

            node = node.next

        return -1

    def remove(self, key: int) -> None:
        keyHash = self._getHash(key)
        node = self.map[keyHash]

        while node.next is not None:
            if node.next.key == key:
                node.next = node.next.next
                return

            node = node.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
