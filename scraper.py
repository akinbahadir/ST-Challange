from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

url1 = r'https://www.mas.gov.sg/investor-alert-list'

options = Options()
prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("detach",True)
options.add_argument("headless")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)    
driver.get(url1)

header = driver.find_element(By.CSS_SELECTOR, "h1.mas-text-h1").text
print(header)
print()
time.sleep(1)

date = "/html/body/div[1]/main/div[2]/div/div/div/div[3]/div/ul/li[{}]/article/header/div/div/div"
company_name = "/html/body/div[1]/main/div[2]/div/div/div/div[3]/div/ul/li[{}]/article/div[1]/div/h2"
button = "/html/body/div[1]/main/div[2]/div/div/div/div[3]/div/ul/li[{}]/article/div[2]/button/div"
div = "/html/body/div[1]/main/div[2]/div/div/div/div[3]/div/ul/li[{}]/article/div[3]//*"

description = "/html/body/div[1]/main/div[2]/div/div/div/div[3]/div/ul/li[{}]/article/div[2]/p"
desc_Button = "/html/body/div[1]/main/div[2]/div/div/div/div[3]/div/ul/li[{}]/article/div[3]/button"
desc_div = "/html/body/div[1]/main/div[2]/div/div/div/div[3]/div/ul/li[{}]/article/div[4]"

for i in range(1,11):
    print(driver.find_element(By.XPATH, date.format(i)).text)
    print(driver.find_element(By.XPATH, company_name.format(i)).text)

    try:
        if check_exists_by_xpath(description.format(i)):
            print(driver.find_element(By.XPATH, description.format(i)).text)
            driver.find_element(By.XPATH, desc_Button.format(i)).click()
            time.sleep(1)    
            print(driver.find_element(By.XPATH, desc_div.format(i)).text)
        else:
            driver.find_element(By.XPATH, button.format(i)).click()
            time.sleep(1)
            print(driver.find_element(By.XPATH, div.format(i)).text)

    except NoSuchElementException:
        print()

    print()
