from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

url = 'https://rent.591.com.tw/'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(5)


# 尋找搜尋框
search_section = browser.find_element(By.XPATH, '//*[@id="rent-list-app"]/div/section[1]/div[3]/input')
search_section.send_keys('淡水區')
time.sleep(3)

# 顯式等待
# 隱式等待

# 按下按鈕
search_button = browser.find_element(By.XPATH, '//*[@id="rent-list-app"]/div/section[1]/div[3]/div')
time.sleep(3)
search_button.click()
time.sleep(3)

# 選擇獨立套房
rent_tao = browser.find_element(By.XPATH, '//*[@id="rent-list-app"]/div/div[2]/section[2]/ul/li[3]')
time.sleep(3)
rent_tao.click()
time.sleep(3)
# 選擇租金
rent_fee = browser.find_element(By.XPATH, '//*[@id="rent-list-app"]/div/div[2]/section[3]/ul/li[2]/i')
time.sleep(3)
rent_fee.click()
time.sleep(3)



content = browser.find_element(By.XPATH, '//*[@id="rent-list-app"]/div/div[3]/div[1]/section[3]/div')
sections = content.find_elements(By.XPATH, './section')

rent_list = []
for section in sections:
    rent_info = {}
    href = section.find_element(By.XPATH, './a').get_attribute('href')
    full_text = section.find_element(By.CLASS_NAME, 'rent-item-right').text
    price_text = section.find_element(By.CLASS_NAME, 'item-price-text').text
    rent_info['href'] = href
    rent_info['full_text'] = full_text
    rent_info['price_text'] = price_text
    rent_list.append(rent_info)

for rent in rent_list:
    print(rent)
    print('=======================================')





