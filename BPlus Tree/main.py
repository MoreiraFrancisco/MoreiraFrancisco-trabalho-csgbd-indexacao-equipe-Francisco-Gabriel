from b_plus_tree import BPlusTree

def main() -> None:
    bptree = BPlusTree(4)

    keys_to_insert = [10, 20, 5, 15, 25, 30, 7, 12, 40, 50, 60, 35]
    for key in keys_to_insert:
        print(f"Inserindo {key}...")
        bptree.insert(key, f"valor_{key}")
        bptree.print_tree()
        print("-" * 20)

    print()
    print("--- Lista das Folhas ---")
    bptree.print_leaves()

    print()
    print("--- Buscando elementos ---")
    print(f"Busca por 15: {bptree.search(15)}")
    print(f"Busca por 99: {bptree.search(99)}")

    print()
    print("--- Removendo elementos ---")
    keys_to_remove = [15, 25, 50]
    for key in keys_to_remove:
        print(f"Removendo {key}...")
        bptree.remove(key)
        bptree.print_tree()
        print("-" * 20)

    print("\n--- Árvore Final ---")
    bptree.print_leaves()
    bptree.print_tree()

if __name__ == "__main__":
    main()
