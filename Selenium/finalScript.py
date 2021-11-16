from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def add_from_category(id, quantities):
    beginning = '//*[@id="js-product-list"]/div[1]/div['
    ending = ']/article/div/a'
    for i in range(5):
        add_to_basket(beginning + str(i+1) + ending, quantities[i])

    driver.execute_script("window.history.go(-1)")


def add_to_basket(product_xpath, quantity):
    product = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, product_xpath))
    )
    product.click()

    quantity_up_btn = driver.find_element(By.XPATH, '/html/body/main/section/div/div/section/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/div/span[3]/button[1]')
    for i in range(quantity-1):
        quantity_up_btn.click()

    add_btn = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button'))
    )
    add_btn.click()

    continue_shopping = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button'))
    )
    continue_shopping.click()
    driver.execute_script("window.history.go(-1)")


def go_to_category(id_category):
    home_page_li = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'category-2'))
    )

    hover = ActionChains(driver).move_to_element(home_page_li)
    hover.perform()

    led_category = driver.find_element(By.ID, id_category)
    led_clickable = led_category.find_element(By.TAG_NAME, 'a')
    led_clickable.click()



driver = webdriver.Chrome('./chromedriver')
driver.get("http://localhost")
driver.maximize_window()

category_nr = 0
quantities_0 = [2, 3, 4, 5, 1]
go_to_category('category-7')
add_from_category(category_nr, quantities_0)

category_nr = 1
quantities_1 = [3, 4, 1, 3, 2]
go_to_category('category-5')
add_from_category(category_nr, quantities_1)

basket = driver.find_element(By.XPATH, '//*[@id="_desktop_cart"]/div/div/a')
basket.click()

remove_from_cart = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[1]/div/div[2]/ul/li[1]/div/div[3]/div/div[3]/div/a'))
    )
remove_from_cart.click()

order_execution = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[2]/div/a')
order_execution.click()



gender = driver.find_element(By.CSS_SELECTOR, "input[name='id_gender'][type='radio'][value='1']")
gender.click()

first_name = driver.find_element(By.CSS_SELECTOR, "input[name='firstname'][type='text']")
first_name.send_keys('boomer')

last_name = driver.find_element(By.CSS_SELECTOR, "input[name='lastname'][type='text']")
last_name.send_keys('rylu')

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
ind = random.randint(0, 25)
email_address = alphabet[ind]
for i in range(4):
    ind = random.randint(26, 35)
    letter = alphabet[ind]
    email_address = email_address + letter

email = driver.find_element(By.CSS_SELECTOR, "input[name='email'][type='email']")
email.send_keys(email_address + '@wp.pl')

password = driver.find_element(By.CSS_SELECTOR, "input[name='password'][type='password']")
password.send_keys('#Abc1234')

birthday = driver.find_element(By.CSS_SELECTOR, "input[name='birthday'][type='text']")
birthday.send_keys('1967-10-22')

newsletter_1 = driver.find_element(By.CSS_SELECTOR, "input[name='optin'][type='checkbox'][value='1']")
newsletter_1.click()

newsletter_2 = driver.find_element(By.CSS_SELECTOR, "input[name='customer_privacy'][type='checkbox'][value='1']")
newsletter_2.click()

newsletter_3 = driver.find_element(By.CSS_SELECTOR, "input[name='newsletter'][type='checkbox'][value='1']")
newsletter_3.click()

newsletter_4 = driver.find_element(By.CSS_SELECTOR, "input[name='psgdpr'][type='checkbox'][value='1']")
newsletter_4.click()

next_btn = driver.find_element(By.CSS_SELECTOR, "button[name='continue'][type='submit'][value='1']")
driver.execute_script("arguments[0].scrollIntoView();", next_btn)
next_btn.click()



address = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='address1'][type='text']"))
    )
address.send_keys('ul. Bikobeara 3')

postcode = driver.find_element(By.CSS_SELECTOR, "input[name='postcode'][type='text']")
postcode.send_keys('12-098')

city = driver.find_element(By.CSS_SELECTOR, "input[name='city'][type='text']")
city.send_keys('Gdańsk')

next_btn = driver.find_element(By.CSS_SELECTOR, "button[name='confirm-addresses'][type='submit'][value='1']")
driver.execute_script("arguments[0].scrollIntoView();", next_btn)
next_btn.click()


ups = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='radio'][id='delivery_option_8']"))
    )
ups.click()

next_btn = driver.find_element(By.CSS_SELECTOR, "button[name='confirmDeliveryOption'][type='submit'][value='1']")
next_btn.click()



cash_on_delivery = driver.find_element(By.CSS_SELECTOR, "input[id='payment-option-2'][type='radio']")
cash_on_delivery.click()

agreement = driver.find_element(By.CSS_SELECTOR, "input[id='conditions_to_approve[terms-and-conditions]'][type='checkbox'][value='1']")
agreement.click()


next_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='payment-confirmation']/div[1]/button"))
    )
next_btn.click()


user = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='_desktop_user_info']/div/a[2]"))
    )
user.click()

status = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "history-link"))
    )
status.click()

status_text = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/table/tbody/tr/td[4]/span"))
    )

print("Status zamówienia:", status_text.text)
driver.quit()