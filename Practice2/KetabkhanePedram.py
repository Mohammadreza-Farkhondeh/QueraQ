import re

persons = input().split(' ')
books = input().split(' ')
p, b = [], []

for i in range(len(persons)):
    p.append('')
for i in range(len(books)):
    b.append('')
prs = dict(zip(persons, p))
bks = dict(zip(books, b))


command = input()
while command != 'end':
    reA = re.search('^assign', command)
    reR = re.search('^return', command)
    reB = re.search('^book', command)
    reO = re.search('^owner', command)
    if reA:
        x, book, name = command.split(' ')
        try: 
            if prs[name]== '':
                if bks[book] != '':
                    print('this book has been already borrowed')
                elif bks[book]== '':
                    prs[name] = book
                    bks[book] = name
                else:
                    print('invalid information')
            elif prs[name] != '':
                if book in bks:
                    print('this person has already borrowed a book')
                else:
                    print('invalid information')
            else:
                print('invalid information')
        except:
            print('invalid information')
    elif reR:
        x, name = command.split(' ')
        try:
            if prs[name] == '':
                print('no book has been borrowed by this person')
            elif prs[name] != '':
                bks[prs[name]]  = ''
                prs[name] = ''
            else:
                print('invalid information')
        except:
            print('invalid information')
    elif reB:
        x, y, name = command.split(' ')
        try:
            if prs[name] == '':
                print('no book has been borrowed by this person')
            elif prs[name] != '':
                print(prs[name])
            else:
                print('invalid information')
        except:
            print('invalid information')
    elif reO:
        x, y, book = command.split(' ')
        try:    
            if bks[book] == '':
                print('no one has borrowed this book')
            elif bks[book] != '':
                print(bks[book])
            else:
                print('invalid information')
        except:
            print('invalid information')
    else:
        print('invalid command')
    command = input()

for i in persons:
    if prs[i] != '':
        print(f'{i}: {prs[i]}')
    else:
        print(f'{i}: -')