import time
from selenium import webdriver

chrome_driver_path = "/Users/nadun/chrome-web-driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id("bigCookie")

while True:
    cookie.click()
    cursor_price = driver.find_element_by_xpath('//*[@id="productPrice0"]')
    no_cursor_price = cursor_price.text
    cookies_amount = driver.find_element_by_xpath('//*[@id="cookies"]')
    no_cookies_amount = cookies_amount.text.split(" ")[0]
    if int(no_cookies_amount) >= int(no_cursor_price):
        product_zero = driver.find_element_by_xpath('//*[@id="product0"]')
        product_zero.click()
        time.sleep(1)
