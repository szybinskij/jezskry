def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, Nazwisko: {}, Wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)


person_print('Adam', 'Nowak', 'Test', age='33')

def fargs(ele1, *ele2):
    print('ele1 ', ele1)
    print('args ', ele2)


def fkwargs(ele1, **ele2):
    print('ele1 ', ele1)
    print('kwargs ', ele2)


def fargsundkwargs(ele1, *ele2, **ele3):
    print('ele1 ', ele1)
    print('args ', ele2)
    print('kwargs ', ele3)


print('fargs')
fargs('Adam', 'Nowak', 'Test', '22')

print('fkwargs')
fkwargs('Adam', a='Nowak', b='Test')

print('fargsundkwargs')
fargsundkwargs('Adam', 'Nowak', 'Test', '22', 'Adam1', a='Nowak1', b='Test1', c='Test2')