import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

menu = {

}


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= options)

# Goes to Net Nutrition Website
driver.get("http://nutrition.myubcard.com/NetNutrition/1")
driver.maximize_window()

driver.implicitly_wait(10)

# Goes to C3 on side menu bar

element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[1]/div[1]/div[2]/table/tbody/tr[7]/td/a')

element.click()

driver.implicitly_wait(10)

# Clicks daily menu

element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div[3]/section/table/tbody/tr[1]/td[1]/a')

element.click()

driver.implicitly_wait(10)

# Clicks dinner

element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div[4]/section/div[2]/div[2]/table/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a')

element.click()

table = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[6]/section/table")
def get_primary_row():
    element = table.find_elements(By.CLASS_NAME, "cbo_nn_itemPrimaryRow")
    for row in element:
        cells = row.find_elements(By.TAG_NAME, "td")

        # print(cells[1].text + '     |     SERVING SIZE : ' + cells[2].text)
        nutrition = {

        }

        nutrition["Serving Size"] = cells[2].text
        menu[cells[1].text] = nutrition


def get_alternate_row():
    rows_2 = table.find_elements(By.CLASS_NAME, "cbo_nn_itemAlternateRow")
    # print(rows_2)
    for row in rows_2:
        cells = row.find_elements(By.TAG_NAME, "td")

        nutrition = {

        }

        nutrition["Serving Size"] = cells[2].text
        menu[cells[1].text] = nutrition


get_primary_row()
get_alternate_row()

print(menu)