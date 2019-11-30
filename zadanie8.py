file = open('zadanie8.txt', 'w+')
file.write('1\n2\n3\n4\n5\n')

file.seek(0)
print(file.read())
file.close()