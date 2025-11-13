from b_plus_tree import BPlusTree
import random

def main() -> None:
    random.seed(None)
    bptree = BPlusTree(4)

    l = list(range(51))
    for i in range(len(l) // 2):
        j = random.randint(0, len(l) - 1)
        aux = l[i]
        l[i] = l[j]
        l[j] = aux

    for i in l:
        print(f'inserting: {i}')
        bptree.insert(i, f'value: {i}')
        bptree.print_tree()
        print('-' * 50)


if __name__ == "__main__":
    main()
