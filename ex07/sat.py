import sys
sys.path.append('../')
from ex03.BooleanEvaluation import eval_formula
import itertools


def sat(formula: str):
    formula_set = set(formula)
    nb_var = sum([x.isupper() for x in formula_set])
    combinations = list(itertools.product([0, 1], repeat=nb_var))
    for k in range(len(combinations)):
        l = 0
        new_formula = ""
        for element in formula:
            if element.isupper():
                if len(combinations[k]) == 1:
                    new_formula += str(combinations[k][0])
                else:
                    new_formula += str(combinations[k][l])
                l+=1
            else:
                new_formula += element
        res = eval_formula(new_formula)
        if res:
            return True
    return False


def main():
    print(sat('AB|'))
    print(sat('AB&'))
    print(sat('AA!&'))
    print(sat('AA^'))

if __name__ == '__main__':
    main()
