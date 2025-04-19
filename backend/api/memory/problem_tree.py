class ProblemNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children: list[ProblemNode] = []

    def has_children(self) -> bool:
        return True if len(self.children) == 0 else False


class ProblemTree:
    """
    ProblemTree:
    A dynamic tree, which is designated to a specific counselor
    and cannot grow past a depth of 3
    """

    def __init__(self, init_node: ProblemNode):
        self.root = init_node

    def insert(self, node: ProblemNode):
        self.root.children.append(node)


if __name__ == "__main__":
    root_node = ProblemNode("root", 0)
