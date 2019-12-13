from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(executable_path=r"D:\chromedriver\chromedriver.exe")
driver.get("https://www.pcprojekt.pl/")
title = driver.title
print("\n\nWitamy na stronie", title)
print("\nWybierzemy komputer dla Ciebie")
time.sleep(3)

try:
    assert "PC Projekt - Komputery gamingowe," \
           " do grania, dla gracza," \
           " smartfony Xiaomi - PC Projekt" in driver.title
except AssertionError:
    print("Ups! To nie jest PcProjekt")
    driver.close()

try:
    driver.find_element_by_xpath("(//a[@type='button'])[2]").click()
    time.sleep(3)
except NoSuchElementException:
    print("Ups! Coś się popsuło...")
    driver.close()

try:
    driver.find_element_by_xpath(
        "//div[@id='pagination']/form/div/button/span").click()
    time.sleep(3)
except NoSuchElementException:
    print("Ups! Coś się zmieniło na stronie "
          "(brak przycisku \"Pokaż Wszystkie\")")
    driver.close()

try:
    driver.find_element_by_link_text(
            "Dom / Biuro Multimedia Core i3-9100F ,...").click()
    time.sleep(3)
except NoSuchElementException:
    print("Ups! Ten komputer nie jest na sprzedaż :(")
    driver.close()

try:
    driver.find_element_by_xpath("//p[@id='add_to_cart']/button/span").click()
    time.sleep(3)
except NoSuchElementException:
    print("Ups! Coś poszło nie tak")
    driver.close()

try:
    print("\n- teraz wypełnij dane, "
          "nie zapomnij o dobrym hasle bo utworzymy ci konto")

    driver.find_element_by_id("email").send_keys("test@test.pl")
    driver.find_element_by_id("create_account").click()
    time.sleep(2)
    driver.find_element_by_id("passwd").send_keys("haselkohaselko12#")
    driver.find_element_by_id("firstname").send_keys("Adam Nowak")
    driver.find_element_by_id("vat_number").send_keys("56748947682")
    driver.find_element_by_id("address1").send_keys("Floriańska 1")
    driver.find_element_by_id("postcode").send_keys("30-300")
    driver.find_element_by_id("city").send_keys("Kraków")
    driver.find_element_by_id("phone_mobile").send_keys("555 666 777")
    print("\n- Wybierz teraz dostawe, sposób płatności, "
          "przeczytaj regulamin i dokonaj zakupu\n\nCzas do zamkniecia - 10s")
    driver.find_element_by_xpath("// a[ @ id = 'submitOrder'] / span").click()
    time.sleep(10)
    driver.close()
except NoSuchElementException:
    print("Ups! Coś poszło nie tak")
    driver.close()
