def eval_set(formula, sets):
    for set in sets:
        if len(sets[0]) != len(set):
            return "Wrong set size"
    for element in formula:
        if element == '!':
            pass
        if element in ('&', '|', '^', '=', '>'):
            if element == '&':
                pass
        else:
            pass


def main():
    sets = [[0, 2, 3], [0, 4, 5]]
    print(eval_set('AB&', sets))

if __name__ == '__main__':
    main()