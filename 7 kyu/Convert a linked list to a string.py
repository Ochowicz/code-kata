def stringify(node):
    if node is None:
        return 'None'

    parts = []
    while node is not None:
        parts.append(str(node.data))
        node = node.next

    return ' -> '.join(parts) + ' -> None'