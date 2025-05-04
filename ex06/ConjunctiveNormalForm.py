import sys
sys.path.append('../')
from cls.ASTNode import ASTNode


def conjunctive_normal_form(formula):
    pass

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
