from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.prompt_for_download': False,
    'download.default_directory': r'D:\Projetos\DownloadHub\relatorios',
    'profile.default_content_setting_values.automatic_downloads': 1,
})

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://consulta-empresa.netlify.app/')
sleep(4)

# --------------------------------------------------------------------#

user = driver.find_element(By.XPATH, "//input[@id='username']")
sleep(1)
user.click()
user.send_keys('jhonatan')

passaword = driver.find_element(By.XPATH, "//input[@id='password']")
sleep(1)
passaword.click()
passaword.send_keys('12345678')

button_login = driver.find_element(
    By.XPATH, "//button[@class='btn btn-primary btn-lg']")
button_login.click()
sleep(2)

# --------------------------------------------------------------------#


def download_company_reports(driver):
    sleep(5)
    company_names = driver.find_elements(
        By.XPATH, "//td[@name='nome_empresa']")
    sleep(2)

    company_perfil_pdf = driver.find_elements(
        By.XPATH, "//button[@class='download-btn']")
    sleep(2)

    for name, button_pdf in zip(company_names, company_perfil_pdf):

        button_pdf.click()
        sleep(2)

        directory = r'D:\Projetos\DownloadHub\relatorios'
        old_name = 'perfil_empresa.pdf'
        new_name = f'{name.text}.pdf'

        old_full_path = os.path.join(directory, old_name)
        new_full_path = os.path.join(directory, new_name)

        os.rename(old_full_path, new_full_path)


download_company_reports(driver=driver)

next_page_button = driver.find_element(By.XPATH, "//button[@id='nextBtn']")

while next_page_button.get_attribute('disabled') == None:
    next_page_button.click()
    download_company_reports(driver=driver)


input('aperte para entra')
