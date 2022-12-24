# 台鐵時刻表查詢
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 台鐵時刻表網址
delay = 1
url = 'https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime'
cd = '依時刻'
ss = '1000-臺北'  # 出發站
es = '1100-中壢'  # 到達站
dd = '2022/12/23'  # 出發日期
dt = '20:00'  # 查詢起時間
et = '23:59'  # 查詢迄時間

driver = webdriver.Chrome()
driver.get(url)
sleep(delay)

# 輸入查詢條件
driver.find_element(By.LINK_TEXT, '依時刻').click()
# 輸入出發站
driver.find_element('id', 'startStation').send_keys(ss)
sleep(delay)
# 輸入到達站
driver.find_element('id', 'endStation').send_keys(es)
sleep(delay)
# 輸入轉乘條件
driver.find_element(By.XPATH, '//*[@id="queryForm"]/div[1]/div[1]/div[5]/div[2]/label[1]').click()
sleep(delay)
# 輸入出發日期
driver.find_element(By.XPATH, '//*[@id="queryForm"]/div[1]/div[2]/div[1]/div[2]/button').click()
driver.find_element('id', 'rideDate').send_keys(dd)
sleep(delay)
# 輸入起訖時間
driver.find_element('id', 'startTime').click()
driver.find_element('id', 'startTime').send_keys(dt)
sleep(delay)
driver.find_element('id', 'endTime').click()
driver.find_element('id', 'endTime').send_keys(et)
sleep(delay)
# 輸入車種
driver.find_element(By.XPATH, '//*[@id="queryForm"]/div[1]/div[3]/div[1]/div[2]/label[1]').click()
sleep(delay)
# 按查詢
driver.find_element(By.XPATH, '//*[@id="queryForm"]/div[1]/div[3]/div[2]/input').click()

data = driver.find_element(By.TAG_NAME, 'tbody')
print('車種車次 (始發站 → 終點站)', '出發時間', '抵達時間', "\t", '行駛時間')
for row in data.find_elements(By.CLASS_NAME, "trip-column"):
    cells = row.find_elements(By.TAG_NAME, "td")
    train_number = cells[0].text
    departure_time = cells[1].text
    arrival_time = cells[2].text
    duration = cells[3].text
    print(train_number, departure_time, "\t", arrival_time, "\t", duration)

driver.close()