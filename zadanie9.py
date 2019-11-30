try:
    with open('zadanie8.txt', 'r') as file, open('zadanie99.txt', 'w+') as file2:
        file2.write(file.read())

except IOError as ioe:
    print(ioe)  # Wypisanie informacji związanej zdanym typem wyjątku.

finally:
    if file:
        file.close()
    if file2:
        file2.close()

print(file.closed)
print(file2.closed)