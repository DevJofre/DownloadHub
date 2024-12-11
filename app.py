from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

drive = webdriver.Chrome()
drive.get('https://consulta-empresa.netlify.app/')
sleep(4)

user = drive.find_element(By.XPATH, "//input[@id='username']")
sleep(1)
user.click()
user.send_keys('jhonatan')

passaword = drive.find_element(By.XPATH, "//input[@id='password']")
sleep(1)
passaword.click()
passaword.send_keys('12345678')

button_login = drive.find_element(
    By.XPATH, "//button[@class='btn btn-primary btn-lg']")
sleep(1)
button_login.click()


input('aperte para entra')
