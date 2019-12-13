from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"D:\chromedriver\chromedriver.exe")
driver.get("https://www.pcprojekt.pl/")
title = driver.title
print(title)
time.sleep(2)
try:
    assert "PC Projekt - Komputery gamingowe, do grania, dla gracza, smartfony Xiaomi - PC Projekt" in driver.title
except AssertionError:
    print("Ups! To nie jest PcProjekt")
    driver.close()
    exit()

elem = driver.find_element_by_xpath("(//a[@type='button'])[2]").click()