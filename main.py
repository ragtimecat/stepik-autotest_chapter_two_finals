import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

price = browser.find_element(By.ID, "price")

book = browser.find_element(By.ID, "book")

WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

book.click()

x = browser.find_element(By.ID, "input_value").text
answer = math.log(abs(12*math.sin(int(x))))

browser.find_element(By.ID, "answer").send_keys(answer)

submit = browser.find_element(By.ID, "solve")
submit.click()

time.sleep(10)
browser.quit()
