# 找出最新一期的，威力彩的期數，開出順序，大小順序，第二區號碼
import requests
from bs4 import BeautifulSoup

url = 'https://www.taiwanlottery.com.tw/index_new.aspx'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

res = requests.get(url=url, headers=headers)
text = BeautifulSoup(res.text, 'html.parser')  # html.parser解析器
# 找出威力彩的開獎區
data = text.find('div', class_='contents_box02')
# print(data)

# 找出威力彩開獎期數
period = data.find('span', 'font_black15').text
print(period)

# 找出開獎號碼，大小順序，第二區特別號
nums = data.find_all('div', class_='ball_tx ball_green')
# print(nums)
print("開出順序:", end='')
for i in range(0, 6):
    print(nums[i].text, end='')

print("\n大小順序:", end='')
for i in range(6, 12):
    print(nums[i].text, end='')

print('\n第二區:', end='')
second = data.find('div', class_='ball_red').text
print(second)





