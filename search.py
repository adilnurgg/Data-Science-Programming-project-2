class Node:
    def __init__(self, key):
        self.key = key
        self.values = []
        self.left = None
        self.right = None

    def __len(self, size):
        size += len(self.values)
        if self.right is not None:
            size += self.right.__len(0)
        if self.left is not None:
            size += self.left.__len(0)
        return size

    def __len__(self):
        size = 0
        return self.__len(size)

    def lookup(self, key):
        curr = self
        while True:
            if key < curr.key:
                if curr.left is not None:
                    curr = curr.left
                else:
                    return []
            elif key > curr.key:
                if curr.right is not None:
                    curr = curr.right
                else:
                    return []
            else:
                return curr.values


class BST:
    def __init__(self):
        self.root = None

    def add(self, key, val):
        if self.root is None:
            self.root = Node(key)

        curr = self.root
        while True:
            if key < curr.key:
                # go left
                if curr.left is None:
                    curr.left = Node(key)
                curr = curr.left
            elif key > curr.key:
                # go right
                if curr.right is None:
                    curr.right = Node(key)
                curr = curr.right
            else:
                # found it!
                assert curr.key == key
                break
        curr.values.append(val)

    def __dump(self, node):
        if node is None:
            return
        self.__dump(node.right)  # 1
        print(node.key, ":", node.values)  # 2
        self.__dump(node.left)  # 3

    def dump(self):
        self.__dump(self.root)

    def __getitem__(self, item):
        return self.root.lookup(item)