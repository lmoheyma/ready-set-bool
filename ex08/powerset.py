def powerset(set):
    if len(set) == 0:
        return [[]]
    cs = []
    for c in powerset(set[1:]):
        cs += [c, c+[set[0]]]
    return cs


def main():
    print(powerset([]))
    print(powerset([1]))
    print(powerset([1, 2, 3]))

if __name__ == '__main__':
    main()
