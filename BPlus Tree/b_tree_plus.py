from typing import Generic, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
    key: list[T]
    child: list['Node[T]']
    is_leaf: bool

    def __init__(self):
        self.key = list()
        self.child = list()

    def __str__(self):
        return str(self.key)

class BTreePlus(Generic[T]):
    root: Node
    min_degree: int

    def __init__(self, min_degree):
        self.root = Node()
        self.root.is_leaf = False
        self.root.key = list()
        self.min_degree = min_degree

    def insert(self, key):
        if len(self.root.key) == (2 * self.min_degree - 1):
            self._split_root()
        self._insert_nonfull(self.root, key)

    def _insert_nonfull(self, node, key):
        if node.is_leaf:
            insert_index = 0
            while insert_index < len(node.key) and key < node.key[insert_index]:
                insert_index = insert_index + 1
            node.key.insert(insert_index, key)
        else:
            insert_index = 0
            while insert_index < len(node.key) and key < node.key[insert_index]:
                insert_index = insert_index + 1
            insert_index = insert_index + 1
            if len(node.child[insert_index].key) == (2 * self.min_degree - 1):
                self._split_child(node, insert_index)
                if key > node.key[insert_index]:
                    insert_index = insert_index + 1
            self._insert_nonfull(node.child[insert_index], key)

    def _split_root(self):
        new_node = Node()
        new_node.is_leaf = False
        new_node.child.append(self.root)
        self.root = new_node
        self._split_child(self.root, 0)
        return new_node

    def _split_child(self, node: Node, index_child: int):
        half = Node()
        child = node.child[index_child]
        half.is_leaf = child.is_leaf
    
        half.key = [None]
        # for i in range(self.min_degree - 1):
        #     half.key[i] = child.key[i + self.min_degree]

        half.key = child.key[self.min_degree:-1]

        if not child.is_leaf:
            # for i in range(self.min_degree):
            #     half.child[i] = child.child[i + self.min_degree]
            half.child = child.child[self.min_degree:-1]

        node.child.insert(index_child + 1, half)
        node.key.insert(index_child, child.key[self.min_degree])

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        i = 0
        while i <= len(node.key) and key > node.key[i]:
            i = i + 1
        if i == node.key[i]:
            return (node.key[i], i)
        elif node.is_leaf:
            return None
        return self._search(node.child[i], key)

def main() -> None:
    n = Node()
    n.key = [1, 2, 3, 4]
    print(n)

if __name__ == '__main__':
    main()
