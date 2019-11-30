def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, Nazwisko: {}, Wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)


person_print('Adam', 'Nowak', 'Test', age='33')

def fargs(ele1, *ele2): #argumenty
    print('ele1 ', ele1)
    print('args ', ele2)


def fkwargs(ele1, **ele2): #nazwa-wartość argumentu
    print('ele1 ', ele1)
    print('kwargs ', ele2)


def fargsundkwargs(ele1, *ele2, **ele3):
    print('ele1 ', ele1)
    print('args ', ele2)
    print('kwargs ', ele3)


print('fargs')                          # Gdy chcemy przekazać dowolną liczbę argumentów pozycyjnych.
fargs('Adam', 'Nowak', 'Test', '22')    # Czyli takich dla których przy wywołaniu funkcji nie podajemy
                                        # ich nazwy, a przypisanie wartości bazuje na kolejności argumentów.

print('fkwargs')                        # gdy do naszej funkcji chcemy przekazywać argumenty,
fkwargs('Adam', a='Nowak', b='Test')    # które wyróżniają się nazwą możemy użyć parametru z dwoma gwiazdkami
                                        # Przekazane w ten sposób argumenty są dostępne w funkcji w postaci słownika.

print('fargsandkwargs')
fargsundkwargs('Adam', 'Nowak', 'Test', '22', 'Adam1', a='Nowak1', b='Test1', c='Test2')