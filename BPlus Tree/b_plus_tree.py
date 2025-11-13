import bisect

class Node:
    order: int
    is_leaf: bool
    keys: list
    children: list
    parent: 'Node | None'
    next: 'Node | None'

    def __init__(self, order, is_leaf=False):
        self.order = order
        self.is_leaf = is_leaf
        self.keys = list()
        self.children = list()
        self.parent = None
        self.next = None

    def is_full(self):
        return len(self.keys) == self.order

    def split_leaf(self):
        mid_index = self.order // 2

        right_sibling = Node(self.order, True)
        right_sibling.parent = self.parent

        right_sibling.keys = self.keys[mid_index:]
        right_sibling.children = self.children[mid_index:]

        copy_up_key = right_sibling.keys[0]

        self.keys = self.keys[:mid_index]
        self.children = self.children[:mid_index]

        right_sibling.next = self.next
        self.next = right_sibling

        return copy_up_key, right_sibling

    def split_internal(self):
        mid_index = self.order // 2

        right_sibling = Node(self.order, False)
        right_sibling.parent = self.parent

        promote_key = self.keys[mid_index]

        right_sibling.keys = self.keys[mid_index + 1:]
        right_sibling.children = self.children[mid_index + 1:]

        for child in right_sibling.children:
            child.parent = right_sibling

        self.keys = self.keys[:mid_index]
        self.children = self.children[:mid_index + 1]

        return promote_key, right_sibling


class BPlusTree:
    root: Node
    order: int

    def __init__(self, order):
        self.root = Node(order, True)
        self.order = order

    def _find_leaf(self, key):
        node = self.root
        while not node.is_leaf:
            idx = bisect.bisect_right(node.keys, key)
            node = node.children[idx]
        return node

    def search(self, key):
        leaf = self._find_leaf(key)
        try:
            idx = leaf.keys.index(key)
            return leaf.children[idx]
        except ValueError:
            return None

    def insert(self, key, value):
        leaf = self._find_leaf(key)
        try:
            idx = leaf.keys.index(key)
            leaf.children[idx] = value
            return
        except ValueError:
            pass

        idx = bisect.bisect_left(leaf.keys, key)
        leaf.keys.insert(idx, key)
        leaf.children.insert(idx, value)

        if leaf.is_full():
            copy_up_key, new_sibling = leaf.split_leaf()
            self._insert_in_parent(leaf, copy_up_key, new_sibling)

    def _insert_in_parent(self, node, key, new_child):
        parent = node.parent
        if parent is None:
            self.root = Node(self.order)
            self.root.keys = [key]
            self.root.children = [node, new_child]
            node.parent = self.root
            new_child.parent = self.root
            return

        idx = bisect.bisect_right(parent.keys, key)
        parent.keys.insert(idx, key)
        parent.children.insert(idx + 1, new_child)

        if parent.is_full():
            promote_key, new_sibling = parent.split_internal()
            self._insert_in_parent(parent, promote_key, new_sibling)

    def remove(self, key):
        leaf = self._find_leaf(key)
        try:
            idx = leaf.keys.index(key)
            leaf.keys.pop(idx)
            leaf.children.pop(idx)
        except ValueError:
            print(f"Chave {key} não encontrada para remoção.")
            return

        min_keys = self.order // 2
        if len(leaf.keys) < min_keys and leaf is not self.root:
            self._rebalance(leaf)

    def _rebalance(self, node):
        parent = node.parent
        if parent is None:

            if not node.is_leaf and not node.keys:
                self.root = node.children[0]
                self.root.parent = None
            return

        child_idx = parent.children.index(node)

        if child_idx > 0:
            left_sibling = parent.children[child_idx - 1]
            if len(left_sibling.keys) > self.order // 2:
                self._borrow_from_left(node, left_sibling, parent, child_idx)
                return

        if child_idx < len(parent.children) - 1:
            right_sibling = parent.children[child_idx + 1]
            if len(right_sibling.keys) > self.order // 2:
                self._borrow_from_right(node, right_sibling, parent, child_idx)
                return

        if child_idx > 0:
            self._merge_nodes(parent.children[child_idx - 1], node, parent, child_idx)
        else:
            self._merge_nodes(node, parent.children[child_idx + 1], parent, child_idx + 1)

    def _borrow_from_left(self, node, sibling, parent, child_idx):
        node.keys.insert(0, sibling.keys.pop())
        node.children.insert(0, sibling.children.pop())
        parent.keys[child_idx - 1] = node.keys[0] if node.is_leaf else sibling.keys[-1]

    def _borrow_from_right(self, node, sibling, parent, child_idx):
        node.keys.append(sibling.keys.pop(0))
        node.children.append(sibling.children.pop(0))
        parent.keys[child_idx] = sibling.keys[0]

    def _merge_nodes(self, left_node, right_node, parent, right_child_idx):
        separator_key = parent.keys.pop(right_child_idx - 1)

        if not left_node.is_leaf:
            left_node.keys.append(separator_key)

        left_node.keys.extend(right_node.keys)
        left_node.children.extend(right_node.children)

        if left_node.is_leaf:
            left_node.next = right_node.next

        parent.children.pop(right_child_idx)

        if len(parent.keys) < self.order // 2 and parent is not self.root:
            self._rebalance(parent)
        elif not parent.keys and parent is self.root:

            self.root = left_node
            left_node.parent = None

    def print_tree(self):
        if not self.root:
            print("A árvore está vazia.")
            return

        queue = [self.root]
        level = 0
        while queue:
            print(f"Nível {level}:")
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                print(f"  {node.keys}", end=" -> ")
                if not node.is_leaf:
                    queue.extend(node.children)
            print("\n")
            level += 1

    def print_leaves(self):
        if not self.root:
            print("A árvore está vazia.")
            return

        node = self.root
        while not node.is_leaf:
            node = node.children[0]

        while node:
            print(f"{node.keys}", end=" -> ")
            node = node.next
        print("Fim")
