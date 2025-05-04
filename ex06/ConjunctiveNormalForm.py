class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

def parse_rpn(expression):
    stack = []
    for token in expression:
        if token in "&|^=>":
            b = stack.pop()
            a = stack.pop()
            stack.append(Node(token, a, b))
        elif token == "!":
            a = stack.pop()
            stack.append(Node(token, a))
        else:
            stack.append(Node(token))
    return stack[0]

def eliminate_implications(node):
    if node is None or node.is_leaf():
        return node

    node.left = eliminate_implications(node.left)
    if node.right:
        node.right = eliminate_implications(node.right)

    if node.value == ">":
        return Node("|", Node("!", node.left), node.right)
    elif node.value == "=":
        a, b = node.left, node.right
        return Node("|",
                    Node("&", a, b),
                    Node("&", Node("!", a), Node("!", b)))
    elif node.value == "^":
        a, b = node.left, node.right
        return Node("|",
                    Node("&", a, Node("!", b)),
                    Node("&", Node("!", a), b))
    else:
        return node

def push_negations(node):
    if node is None or node.is_leaf():
        return node
    if node.value == "!":
        child = node.left
        if child.value == "!":
            return push_negations(child.left)
        elif child.value == "&":
            return Node("|", push_negations(Node("!", child.left)), push_negations(Node("!", child.right)))
        elif child.value == "|":
            return Node("&", push_negations(Node("!", child.left)), push_negations(Node("!", child.right)))
        else:
            return Node("!", push_negations(child))
    else:
        node.left = push_negations(node.left)
        if node.right:
            node.right = push_negations(node.right)
        return node

def distribute_or_over_and(node):
    if node is None or node.is_leaf():
        return node

    node.left = distribute_or_over_and(node.left)
    if node.right:
        node.right = distribute_or_over_and(node.right)

    if node.value == "|":
        A, B = node.left, node.right
        if B and B.value == "&":
            return Node("&",
                        distribute_or_over_and(Node("|", A, B.left)),
                        distribute_or_over_and(Node("|", A, B.right)))
        if A and A.value == "&":
            return Node("&",
                        distribute_or_over_and(Node("|", A.left, B)),
                        distribute_or_over_and(Node("|", A.right, B)))
    return node


def to_rpn(node):
    if node.is_leaf():
        return node.value
    elif node.value == "!":
        return to_rpn(node.left) + "!"
    else:
        return to_rpn(node.left) + to_rpn(node.right) + node.value

def conjunctive_normal_form(expr):
    tree = parse_rpn(expr)
    tree = eliminate_implications(tree)
    tree = push_negations(tree)
    tree = distribute_or_over_and(tree)
    return to_rpn(tree)

def main():
    print(conjunctive_normal_form('AB&!'))
    print(conjunctive_normal_form('AB|!'))
    print(conjunctive_normal_form('AB|C&'))
    print(conjunctive_normal_form('AB|C|D|'))
    print(conjunctive_normal_form('AB&C&D&'))
    print(conjunctive_normal_form('AB&!C!|'))
    print(conjunctive_normal_form('AB|!C!&'))


if __name__ == '__main__':
    main()
