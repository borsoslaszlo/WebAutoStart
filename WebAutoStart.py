from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)

main_window = driver.current_window_handle

driver.get('https://mail.google.com')
usernameField = driver.find_element_by_name('identifier')  
usernameField.send_keys('Type the password here' + Keys.RETURN)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))


passwordField =  driver.find_element_by_name('password')
passwordField.send_keys('Type the password here' + Keys.RETURN)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.NAME, 'q')))

driver.execute_script('''window.open("https://facebook.com", "_blank");''')


for handle in driver.window_handles:
    driver.switch_to_window(handle)



usernameField = driver.find_element_by_name('email')
usernameField.send_keys('boki@freemail.hu')

passwordField =  driver.find_element_by_name('pass')
passwordField.send_keys('P4ssw0rd4F4c3b00k' + Keys.RETURN)

driver.execute_script('''window.open("https://messenger.com", "_blank");''')

for handle in driver.window_handles:
    driver.switch_to_window(handle)
'''
usernameField = driver.find_element_by_name('email')
usernameField.send_keys('boki@freemail.hu')

passwordField =  driver.find_element_by_name('pass')
passwordField.send_keys('P4ssw0rd4F4c3b00k' + Keys.RETURN)
'''





