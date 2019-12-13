import smtplib

try:
    server_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    server_smtp.starttls()
    server_smtp.login('pythontest456', 'python456')
    topic = input("Temat:")
    body = input("Tresc:")
    if not topic or not body:
        print("Puste wiadomosci lub temat")
        exit()
    msg = 'Subject:{}\n\n{}'.format(topic,body)
    sendmail = server_smtp.sendmail('python456',input("Wyslij do:\n"),msg)
    print("Wyslano")

except IOError:
    print("Błąd")
