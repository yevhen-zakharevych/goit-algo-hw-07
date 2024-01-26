from ddp import Node, insert


def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current.val


if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    max_value = max_value_node(root)
    print(f"Max value: {max_value}")
