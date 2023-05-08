import random


def ls(string):
    mystring = string
    keyword = 'candidate: '
    before_keyword, keyword, after_keyword = mystring.partition(keyword)
    return str(after_keyword)


inp1 = ls(input())
X = input()
inp2 = ls(input())
X = input()
inp3 = ls(input())
X = input()
inp4 = ls(input())

liste = [inp1, inp2, inp3, inp4]
print(liste)
print(random.choice(liste))
