import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def import_to_store(file):
    call = 0
    option = Select(driver.find_element(By.ID, 'entity'))
    if file == 'categories.csv':
        option.select_by_value('0')
    elif file == 'products.csv':
        option.select_by_value('1')
        call = 1
    else:
        option.select_by_value('2')
        call = 2

    upload_file = driver.find_element(By.ID, "file")
    upload_file.send_keys("/home/przemoc31/Desktop/Selenium/" + file)

    field_separator = driver.find_element(By.ID, "separator")
    value = "&"
    driver.execute_script("arguments[0].setAttribute('value',arguments[1])", field_separator, value)

    multi_val_separator = driver.find_element(By.ID, "multiple_value_separator")
    value = "&"
    driver.execute_script("arguments[0].setAttribute('value', arguments[1])", multi_val_separator, value)

    elem = driver.find_element(By.XPATH,
                               "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[1]/div[12]/div")
    driver.execute_script("arguments[0].scrollIntoView();", elem)

    yes_delete = driver.find_element(By.ID, "truncate_1")
    if call == 1 or call == 2:
        no_match_ref = driver.find_element(By.ID, "match_ref_0")
    if call == 0 or call == 1:
        no_regenerate = driver.find_element(By.ID, "regenerate_0")
    if call == 0 or call == 1:
        no_force = driver.find_element(By.ID, "forceIDs_0")
    no_mail = driver.find_element(By.ID, "sendemail_0")
    next_step_button = driver.find_element(By.XPATH,
                                         "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[2]/div/button")

    driver.execute_script('arguments[0].click()', yes_delete)
    if call == 1 or call == 2:
        driver.execute_script('arguments[0].click()', no_match_ref)
    if call == 0 or call == 1:
        driver.execute_script('arguments[0].click()', no_regenerate)
    if call == 0 or call == 1:
        driver.execute_script('arguments[0].click()', no_force)
    driver.execute_script('arguments[0].click()', no_mail)
    time.sleep(1)
    driver.execute_script('arguments[0].click()', next_step_button)

    WebDriverWait(driver, 100).until(EC.alert_is_present())
    al = driver.switch_to.alert
    al.accept()

    select = Select(driver.find_element(By.ID, 'valueImportMatchs'))
    select.select_by_value('id|category|description|file_url|price_tin|name')

    rows_to_skip = driver.find_element(By.ID, 'skip')
    rows_to_skip.clear()
    rows_to_skip.send_keys('1')

    if call == 0:
        fields_for_categories()
    elif call == 1:
        fields_for_products()
    else:
        fields_for_combinations()

    import_btn = driver.find_element(By.ID, 'import')
    import_btn.click()

    close = WebDriverWait(driver, 50000).until(
        EC.element_to_be_clickable((By.ID, 'import_close_button')))
    close.click()


def fields_for_categories():
    select = Select(driver.find_element(By.ID, 'type_value[0]'))
    select.select_by_value('no')

    select = Select(driver.find_element(By.ID, 'type_value[1]'))
    select.select_by_value('id')

    select = Select(driver.find_element(By.ID, 'type_value[2]'))
    select.select_by_value('name')

    select = Select(driver.find_element(By.ID, 'type_value[3]'))
    select.select_by_value('description')


def fields_for_products():
    select = Select(driver.find_element(By.ID, 'type_value[0]'))
    select.select_by_value('id')

    select = Select(driver.find_element(By.ID, 'type_value[1]'))
    select.select_by_value('no')

    select = Select(driver.find_element(By.ID, 'type_value[2]'))
    select.select_by_value('name')

    select = Select(driver.find_element(By.ID, 'type_value[3]'))
    select.select_by_value('image')

    select = Select(driver.find_element(By.ID, 'type_value[4]'))
    select.select_by_value('price_tex')

    select = Select(driver.find_element(By.ID, 'type_value[5]'))
    select.select_by_value('description')

    right_btn = driver.find_element(By.ID, "btn_right")
    driver.execute_script("arguments[0].scrollIntoView();", right_btn)
    right_btn.click()

    select = Select(driver.find_element(By.ID, 'type_value[6]'))
    select.select_by_value('category')

    select = Select(driver.find_element(By.ID, 'type_value[7]'))
    select.select_by_value('quantity')

    left_btn = driver.find_element(By.ID, "btn_left")
    driver.execute_script("arguments[0].scrollIntoView();", left_btn)
    left_btn.click()


def fields_for_combinations():
    select = Select(driver.find_element(By.ID, 'type_value[0]'))
    select.select_by_value('no')

    select = Select(driver.find_element(By.ID, 'type_value[1]'))
    select.select_by_value('id_product')

    select = Select(driver.find_element(By.ID, 'type_value[2]'))
    select.select_by_value('product_reference')

    select = Select(driver.find_element(By.ID, 'type_value[3]'))
    select.select_by_value('group')

    select = Select(driver.find_element(By.ID, 'type_value[4]'))
    select.select_by_value('attribute')

    select = Select(driver.find_element(By.ID, 'type_value[5]'))
    select.select_by_value('quantity')


driver = webdriver.Chrome('./chromedriver')
driver.get('http://localhost/admin776jdno0g')
driver.maximize_window()

login = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "passwd")
submit = driver.find_element(By.ID, "submit_login")

login.send_keys("kuba.sachajko@gmail.com")
password.send_keys("1234qwer")
submit.click()


nav = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.ID, 'nav-sidebar')))

driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", nav)
advanced = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="subtab-AdminAdvancedParameters"]')))
clickableLink = advanced.find_element(By.TAG_NAME, "a")
clickableLink.click()
print("es?")

products = driver.find_element(By.ID, "subtab-AdminImport")
clickableLink = products.find_element(By.TAG_NAME, "a")
time.sleep(1)
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", nav)
clickableLink.click()
print("es2?")


import_to_store('categories.csv')
close = WebDriverWait(driver, 500).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main-div"]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[1]/div[7]/button')))
close.click()

import_to_store('products.csv')
close = WebDriverWait(driver, 500).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main-div"]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[1]/div[7]/button')))
close.click()
import_to_store('combinations.csv')

time.sleep(1)
catalog = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.ID, 'subtab-AdminCatalog')))
clickableLink = catalog.find_element(By.TAG_NAME, "a")
clickableLink.click()

attrs = WebDriverWait(driver, 500).until(
    EC.element_to_be_clickable((By.ID, 'subtab-AdminParentAttributesGroups')))
clickableLink = attrs.find_element(By.TAG_NAME, "a")
clickableLink.click()

look = driver.find_element(By.XPATH, '//*[@id="tr_2_1_0"]/td[5]/div/div/button')
look.click()
edit = driver.find_element(By.XPATH, '//*[@id="tr_2_1_0"]/td[5]/div/div/ul/li[1]/a')
edit.click()
select = Select(driver.find_element(By.ID, 'group_type'))
select.select_by_value('select')

save = driver.find_element(By.ID, 'attribute_group_form_submit_btn')
save.click()

driver.quit()
