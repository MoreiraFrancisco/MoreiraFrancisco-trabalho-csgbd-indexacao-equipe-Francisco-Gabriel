class BPlusLeaf:
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.values = []
        self.next = None  # ponteiro para a próxima folha

    def is_full(self):
        return len(self.keys) >= self.order


class BPlusInternal:
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.children = []

    def is_full(self):
        return len(self.keys) >= self.order


class BPlusTree:
    def __init__(self, order: int):
        """Inicializa a árvore com a ordem especificada."""
        self.order = order
        self.root = BPlusLeaf(order)

    def search(self, key: int):
        """Retorna o valor da chave, se existir."""
        node = self.root

        # Descer até a folha
        while isinstance(node, BPlusInternal):
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            node = node.children[i]

        # Procurar dentro da folha
        for i, k in enumerate(node.keys):
            if k == key:
                return node.values[i]

        return None

    def insert(self, key: int, value: any):
        """Insere (chave, valor) na árvore."""
        root = self.root

        # Se raiz é folha
        if isinstance(root, BPlusLeaf):
            split_key, new_node = self._insert_leaf(root, key, value)
            if new_node:  
                # criar nova raiz
                new_root = BPlusInternal(self.order)
                new_root.keys = [split_key]
                new_root.children = [root, new_node]
                self.root = new_root
            return

        # Se raiz é interna
        split = self._insert_internal(root, key, value)
        if split:
            key_split, new_child = split
            new_root = BPlusInternal(self.order)
            new_root.keys = [key_split]
            new_root.children = [root, new_child]
            self.root = new_root

    def _insert_leaf(self, leaf, key, value):
        """Insere em uma folha."""
        # Inserção ordenada
        i = 0
        while i < len(leaf.keys) and leaf.keys[i] < key:
            i += 1

        leaf.keys.insert(i, key)
        leaf.values.insert(i, value)

        # Se não houve overflow
        if not leaf.is_full():
            return None, None

        # Split da folha
        mid = len(leaf.keys) // 2

        new_leaf = BPlusLeaf(self.order)
        new_leaf.keys = leaf.keys[mid:]
        new_leaf.values = leaf.values[mid:]
        new_leaf.next = leaf.next

        leaf.keys = leaf.keys[:mid]
        leaf.values = leaf.values[:mid]
        leaf.next = new_leaf

        # chave que sobe
        return new_leaf.keys[0], new_leaf

    def _insert_internal(self, node, key, value):
        """Insere recursivamente em nós internos."""
        i = 0
        while i < len(node.keys) and key >= node.keys[i]:
            i += 1

        child = node.children[i]

        if isinstance(child, BPlusLeaf):
            split_key, new_node = self._insert_leaf(child, key, value)
        else:
            split = self._insert_internal(child, key, value)
            if split:
                split_key, new_node = split
            else:
                return None

        if new_node:
            node.keys.insert(i, split_key)
            node.children.insert(i + 1, new_node)

            if node.is_full():
                return self._split_internal(node)

        return None

    def _split_internal(self, node):
        """Divide um nó interno."""
        mid = len(node.keys) // 2
        promote_key = node.keys[mid]

        new_node = BPlusInternal(self.order)
        new_node.keys = node.keys[mid + 1:]
        new_node.children = node.children[mid + 1:]

        node.keys = node.keys[:mid]
        node.children = node.children[:mid + 1]

        return promote_key, new_node

    def remove(self, key: int):
        """Remoção simples."""
        leaf = self._find_leaf(self.root, key)
        if leaf is None:
            return False

        if key not in leaf.keys:
            return False

        idx = leaf.keys.index(key)
        leaf.keys.pop(idx)
        leaf.values.pop(idx)
        return True

    def _find_leaf(self, node, key):
        """Percorre até encontrar a folha onde a chave deveria estar."""
        while isinstance(node, BPlusInternal):
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            node = node.children[i]
        return node

    def display(self):
        """Exibe a árvore B+ nível por nível."""
        level = [self.root]
        h = 0

        while level:
            print(f"Nível {h}: ", end="")
            next_level = []
            for node in level:
                if isinstance(node, BPlusLeaf):
                    print(f"[Leaf: {node.keys}]", end="  ")
                else:
                    print(f"[Internal: {node.keys}]", end="  ")
                    next_level.extend(node.children)

            print()
            level = next_level
            h += 1
import random

def teste_bplustree():
    print("=============================================")
    print(" TESTE DA ÁRVORE B+ (Inserções e Remoções)")
    print("=============================================")

    # Ordem da Árvore B+
    order = 4
    arvore = BPlusTree(order)

    # Geração de chaves inteiras entre 1 e 50 em ordem aleatória
    chaves = list(range(1, 51))
    random.shuffle(chaves)

    print("\n=== INSERÇÃO DAS CHAVES (1 a 50) EM ORDEM ALEATÓRIA ===\n")
    print("Sequência aleatória utilizada:", chaves, "\n")

    # Inserção das chaves com exibição da estrutura após cada operação
    for k in chaves:
        print(f"\n>>> Inserindo chave {k}")
        arvore.insert(k, f"valor-{k}")
        arvore.display()

    print("\n=============================================")
    print(" REMOÇÕES (10 chaves selecionadas aleatoriamente)")
    print("=============================================\n")

    # Seleção de 10 chaves aleatórias para remoção
    remover = random.sample(range(1, 51), 10)
    print("Chaves selecionadas para remoção:", remover, "\n")

    for k in remover:
        print(f"\n>>> Removendo chave {k}")
        removido = arvore.remove(k)

        if removido:
            print(f"Chave {k} removida com sucesso.")
        else:
            print(f"Chave {k} não está presente na árvore.")
        
        arvore.display()

    print("\n=============================================")
    print(" TESTE FINALIZADO")
    print("=============================================")


# Execução dos testes
teste_bplustree()

