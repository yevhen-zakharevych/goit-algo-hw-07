from ddp import Node, insert


def sum_node_values(root):
    if root:
        return root.val + sum_node_values(root.left) + sum_node_values(root.right)
    return 0


if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    res = sum_node_values(root)

    print(f"Sum of node values: {res}")