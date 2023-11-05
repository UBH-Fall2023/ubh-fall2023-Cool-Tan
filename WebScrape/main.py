import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

menu = {

}

header_array = []


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

def get_check_box():
    rows = driver.find_elements(By.CSS_SELECTOR, "td.cbo_nn_itemCheckBox")

    for row in rows:
        # Find the checkbox element within each row
        checkbox = row.find_element(By.CSS_SELECTOR, "input[type='checkbox']")

        # Check the checkbox if it's not already checked
        if not checkbox.is_selected():
            checkbox.click()

def get_primary_row():
    element = table.find_elements(By.CLASS_NAME, "cbo_nn_itemPrimaryRow")
    for row in element:
        cells = row.find_elements(By.TAG_NAME, "td")

        # print(cells[1].text + '     |     SERVING SIZE : ' + cells[2].text)
        nutrition = {

        }

        nutrition["Serving Size"] = cells[2].text
        menu[cells[1].text] = nutrition

        #cells[0].click()
        # cells[0].find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div[6]/section/table/tbody/tr[3]/td[1]/input').click()



def get_alternate_row():
    rows_2 = table.find_elements(By.CLASS_NAME, "cbo_nn_itemAlternateRow")
    # print(rows_2)
    for row in rows_2:
        cells = row.find_elements(By.TAG_NAME, "td")

        nutrition = {

        }

        nutrition["Serving Size"] = cells[2].text
        menu[cells[1].text] = nutrition


# get_primary_row()
# get_alternate_row()

get_check_box()

#click_add_items = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div[6]/section/div[4]/table/tbody/tr/td[3]/button')
# click_add_items.click()

click_meal_nutrition = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div[6]/section/div[3]/table/tbody/tr/td[2]/button')
click_meal_nutrition.click()



def search_menu_table():
    menu_table = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/table')

    header_items = menu_table.find_elements(By.CLASS_NAME, 'cbo_nn_NutritionGridHeaderText')

    for header in header_items:
        if header.text.find('%') == -1:
            header_array.append(header.text)

    grid_row = menu_table.find_elements(By.CLASS_NAME, 'cbo_nn_NutritionGridDetailRow')

    for item in grid_row:
        food_name = item.find_element(By.CLASS_NAME, 'cbo_nn_NutritionGridItemName')
        #print(food_name.text)

        values = item.find_elements(By.CLASS_NAME, 'cbo_nn_NutritionGridData')
        values_array = []

        nutrition = {

        }

        for i in range(len(values)):
            nutrition[header_array[i]] = values[i].text

        menu[food_name.text] = nutrition

        #print(header_array)
        #print(values_array)


    #food_rows = menu_table.find_elements(By.CLASS_NAME, 'cbo_nn_NutritionGridData')
    #nutrition_rows = menu_table.find_elements(By.CLASS_NAME, 'cbo_nn_NutritionGridData align-middle')

    #print(nutrition_rows)

    #for nutrition in nutrition_rows:
     #   print(nutrition.text)

    #for food in food_rows:
     #   print(food.text)



search_menu_table()

#print(menu)

def stringify():
    response = ''

    for key in menu.keys():
        #print(key)
        response = response + ' | ' + key + ' : '
        response += ' ('

        values = menu.get(key)
        for value in values.keys():
            response += ' ' + value + ' : '

            response += ' ' + values.get(value) + ', '

        response += ' )'



    return response

