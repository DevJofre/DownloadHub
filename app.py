from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

drive = webdriver.Chrome()
drive.get('https://consulta-empresa.netlify.app/')

login = drive.find_element(By.XPATH, "//input[@id='username']")
sleep(1)
senha = drive.find_element(By.XPATH, "//input[@id='password']")
sleep(1)
entra = drive.find_element(By.XPATH, "//class[@id='btn btn-primary btn-lg']")
sleep(1)

input('aperte para entra')
