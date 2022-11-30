from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

url2 = r'https://www.afdb.org/en/projects-operations/debarment-and-sanctions-procedures'

path = "//*[@id=\"datatable-1\"]"

options = Options()
# prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
# options.add_experimental_option("prefs", prefs)
# options.add_experimental_option("useAutomationExtension", False)
# options.add_experimental_option("excludeSwitches",["enable-automation"])
# options.add_experimental_option("detach",True)
options.add_argument("headless")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)    
driver.get(url2)



print(driver.find_element(By.XPATH, path).text)
