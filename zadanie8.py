file = open('zadanie8.txt', 'w+')
file.write('1\n2\n3\n4\n5\n')

file.seek(0) #przesuwa aktualną pozycję od której następuje czytanie lub pisanie na numer podany w bajtach
print(file.read())
file.close()
