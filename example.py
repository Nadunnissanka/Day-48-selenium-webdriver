from selenium import webdriver
# to press enter
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/nadun/chrome-web-driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.com/Seagate-Portable-External-Hard-Drive/dp/B07X3XGG3F/ref=lp_16225007011_1_2?th=1")

# get price data from amazon web page
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)

# select amazon search input using name
search_bar = driver.find_element_by_name("field-keywords")
print(search_bar.tag_name)
print(search_bar.get_attribute("type"))

# select an element using css selector
link = driver.find_element_by_css(".link a")
print(link.text)

# copy Xpath by inspecting implementation
career = driver.find_element_by_xpath('//*[@id="navFooter"]/div[1]/div/div[1]/ul/li[1]/a')
print(career.text)

# identify by link text
about = driver.find_element_by_link_text("About")
# to click on the link
about.click()

# identify input (use name property)
search = driver.find_element_by_name("search")
search.send_keys("Python")
# to press enter after the
search.send_keys(Keys.ENTER)

driver.quit()
