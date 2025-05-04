import sys
sys.path.append('../')
from cls.ASTNode import ASTNode


def negation_normal_form(formula):
	def preprocessing(formula: str):
		special_cases = {
			'AB>': 'A!B|',
			'AB=': 'AB&A!B!&|'
		}
		for case in special_cases:
			if case in formula:
				startIndex = formula.find(case)
				formula = formula[:startIndex] + special_cases[case] + formula[startIndex + 3:]
		return formula
	symbols = {
		'&': '|',
		'|': '&'
	}
	res = ''
	formula = preprocessing(formula)
	if formula[-1] == '!':
		for element in formula:
			if element.isalpha():
				res += element + '!'
			if element in symbols:
				res += symbols[element]
	return res or formula


def main():
	print(negation_normal_form('AB&!'))
	print(negation_normal_form('AB|!'))
	print(negation_normal_form('AB>'))
	print(negation_normal_form('AB='))
	print(negation_normal_form('AB|C&!'))
	

if __name__ == '__main__':
	main()
