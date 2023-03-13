from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chromedriver_path = "/Users/jonathanchng/Downloads/chromedriver_mac64/chromedriver"
url = "https://tinder.com/"

driver = webdriver.Chrome(chromedriver_path)
driver.get(url)
main_page = driver.current_window_handle


time.sleep(15)

login = driver.find_element(By.XPATH, '//*[@id="s-1432688076"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(15)

print("trying to click")
gmail = driver.find_element(By.XPATH, '//*[@id="s-1211347640"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
gmail.click()

time.sleep(15)

for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle
        driver.switch_to.window(login_page)

time.sleep(5)
time.sleep(5)
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys()

password_input = driver.find_element(By.NAME, "pass")
password_input.send_keys()
time.sleep(2)
password_input.send_keys(Keys.ENTER)

time.sleep(60)



driver.quit()
