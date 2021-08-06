from selenium import webdriver

chrome_driver_path = "/Users/nadun/chrome-web-driver/chromedriver"
index = 0
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

# Challenge 01: Get events from python.org
event_date = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
event_name = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')

event_dict = {}

for date in event_date:
    date_time = date.get_attribute("datetime").split("T")
    date_of_event = date_time[0]
    for event in event_name:
        event_name_fetch = event.text
        fetch_dict = {"time": date_of_event, "event": event_name_fetch}
        event_dict[index] = fetch_dict
        index += 1

print(event_dict)

