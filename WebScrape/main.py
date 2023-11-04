import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= options)

driver.get("http://nutrition.myubcard.com/NetNutrition/1")
driver.maximize_window()

driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[1]/div[1]/div[2]/table/tbody/tr[7]/td/a')

element.click()

driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div[3]/section/table/tbody/tr[1]/td[1]/a')

element.click()

driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div[4]/section/div[2]/div[2]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a')

element.click()