from selenium import webdriver

chrome_driver_path = "/Users/nadun/chrome-web-driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element_by_name("fName")
first_name_input.send_keys("Nadun")
last_name_input = driver.find_element_by_name("lName")
last_name_input.send_keys("Nissanka")
email_input = driver.find_element_by_name("email")
email_input.send_keys("nadunnissanka@icloud.com")
sign_up = driver.find_element_by_xpath('/html/body/form/button')
sign_up.click()
