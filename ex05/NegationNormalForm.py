class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return not self.left and not self.right

def parse_rpn(rpn):
    stack = []
    for token in rpn:
        if token in ('&', '|', '>', '=', '^'):
            if len(stack) < 2:
                raise ValueError(f"Not enough operands for binary operator '{token}'")
            b = stack.pop()
            a = stack.pop()
            stack.append(Node(token, a, b))
        elif token == '!':
            if len(stack) < 1:
                raise ValueError("Not enough operands for unary operator '!'")
            a = stack.pop()
            stack.append(Node('!', a))
        else:
            stack.append(Node(token))
    if len(stack) != 1:
        raise ValueError(f"Invalid RPN expression: leftover stack: {[n.value for n in stack]}")
    return stack[0]


def eliminate_implications(node):
    if node is None:
        return None
    if node.value == '>':
        return Node('|', Node('!', eliminate_implications(node.left)), eliminate_implications(node.right))
    elif node.value == '=':
        A = eliminate_implications(node.left)
        B = eliminate_implications(node.right)
        left = Node('&', A, B)
        right = Node('&', Node('!', A), Node('!', B))
        return Node('|', left, right)
    elif node.value == '^':
        A = eliminate_implications(node.left)
        B = eliminate_implications(node.right)
        left = Node('&', A, Node('!', B))
        right = Node('&', Node('!', A), B)
        return Node('|', left, right)
    elif node.value == '!':
        return Node('!', eliminate_implications(node.left))
    else:
        return Node(node.value,
                    eliminate_implications(node.left),
                    eliminate_implications(node.right))

def to_nnf(node):
    if node is None:
        return None
    if node.value == '!':
        child = node.left
        if child.value == '!':
            return to_nnf(child.left)
        elif child.value == '&':
            return Node('|', to_nnf(Node('!', child.left)), to_nnf(Node('!', child.right)))
        elif child.value == '|':
            return Node('&', to_nnf(Node('!', child.left)), to_nnf(Node('!', child.right)))
        else:
            return Node('!', to_nnf(child))
    elif node.value in ('&', '|'):
        return Node(node.value, to_nnf(node.left), to_nnf(node.right))
    else:
        return node

def to_rpn(node):
    if node.is_leaf():
        return node.value
    elif node.value == '!':
        return to_rpn(node.left) + '!'
    else:
        return to_rpn(node.left) + to_rpn(node.right) + node.value

def negation_normal_form(expr):
    tree = parse_rpn(expr)
    tree = eliminate_implications(tree)
    tree = to_nnf(tree)
    return to_rpn(tree)

if __name__ == "__main__":
    try:
        print(negation_normal_form('AB&!'))
        print(negation_normal_form('AB|!'))
        print(negation_normal_form('AB>'))
        print(negation_normal_form('AB='))
        print(negation_normal_form('AB|C&!'))
    except ValueError as e:
        print(e)
