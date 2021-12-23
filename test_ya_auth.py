from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C://chromedriver.exe')
driver.get('https://passport.yandex.ru/auth')
elem = driver.find_element_by_name('login')
time.sleep(2)
elem.send_keys('test.ya')
time.sleep(2)
elem.send_keys(Keys.RETURN)
time.sleep(2)
elem = driver.find_element_by_name('qwerty')
time.sleep(2)
elem.send_keys('Sinichka2012')
time.sleep(2)
elem.send_keys(Keys.RETURN)
time.sleep(2)
assert 'No results found' not in driver.page_source
driver.close()
driver.quit()

