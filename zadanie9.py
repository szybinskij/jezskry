try:
    with open('zad9a.txt', 'r') as txt_file, open('zad9b.txt', 'w') as txt_file2:
        txt_file2.write(txt_file.read())

except IOError as ioe:
    print(ioe)

finally:
    if txt_file:
        txt_file.close()
    if txt_file2:
        txt_file2.close()

print(txt_file.closed)
print(txt_file2.closed)
