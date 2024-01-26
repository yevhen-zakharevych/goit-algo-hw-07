from ddp import Node, insert


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current.val


if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    min_value = min_value_node(root);
    print(f"Min value: {min_value}")
