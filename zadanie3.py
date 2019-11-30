paswd = 'alamakota'
for x in range(6):
    tryx = input('podaj haslo:')
    if tryx == paswd:
        print('Jestes zwyciezca')
        break
    else:
        continue
else:
    print('Jestes przegranym')
