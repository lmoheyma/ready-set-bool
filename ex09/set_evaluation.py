def eval_set(expr: str, sets: list[set[int]]) -> set[int]:
    stack = []
    universal = set().union(*sets)

    for token in expr:
        if token.isalpha() and token.isupper():
            index = ord(token) - ord('A')
            stack.append(sets[index])
        elif token == '&':
            b = stack.pop()
            a = stack.pop()
            stack.append(a & b)
        elif token == '|':
            b = stack.pop()
            a = stack.pop()
            stack.append(a | b)
        elif token == '^':
            b = stack.pop()
            a = stack.pop()
            stack.append(a ^ b)
        elif token == '=':
            b = stack.pop()
            a = stack.pop()
            stack.append({0} if a == b else set())
        elif token == '>':
            b = stack.pop()
            a = stack.pop()
            stack.append({0} if a < b else set()) 
        elif token == '!':
            a = stack.pop()
            stack.append(universal - a)
        else:
            raise ValueError(f"Invalid token: {token}")
    
    return stack[-1] if stack else set()


def main():
    try:
        sets = [{0, 2, 3}, {0, 4, 5}]
        print(eval_set('AB&', sets))

        sets = [{0, 1, 2}, {3, 4, 5}]
        print(eval_set('AB|', sets))

        sets = [{0, 1, 2}]
        print(eval_set('A!', sets))
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()