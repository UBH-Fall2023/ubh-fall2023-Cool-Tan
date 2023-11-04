from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= options)

driver.get("http://nutrition.myubcard.com/NetNutrition/1")
driver.maximize_window()

element = driver.find_element_by_xpath('//*[@id="sideUnitPanel"]/div[2]/table/tbody/tr[7]/td/a')

element.click()