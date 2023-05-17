import re


def find(exp, operator):
    pattern = r"(\w+)(%s)(\w+)" % operator
    match = re.search(pattern, exp)
    if match:
        start = match.start(1)
        end = match.end(3)
        if exp[0] == '-':
            start = 0
        return start, end

def calculate(exp_with_one_operator):
    answer = eval(exp_with_one_operator)
    return answer

def replace(exp, start, end, result):
    new_exp = exp[:start]+str(result)+exp[end:]
    return new_exp


operators = ['*', '-', '+']
exp = input()

for operator in operators:
    while operator in exp[1:]:
        start, end = find(exp, '\\'+operator)
        exp_with_one_operator = exp[start:end]
        result = calculate(exp_with_one_operator)
        exp = replace(exp, start, end, result)
print(exp)
