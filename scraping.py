import requests
from bs4 import BeautifulSoup

raw = requests.get('https://www1.president.go.kr/petitions')
html = BeautifulSoup(raw.text, "html.parser")


petitions = html.find_element_by_xpath('//*[@id="cont_view"]/div[2]/div/div/div[2]/div[2]/div[4]/div')
#petitions = html.select('div.ct_list1')

number = html.find_element_by_xpath('//*[@id="cont_view"]/div[2]/div/div/div[2]/div[2]/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[1]/span')\
type = html.find_element_by_xpath('//*[@id="cont_view"]/div[2]/div/div/div[2]/div[2]/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[2]')

title = html.find_element_by_xpath('//*[@id="cont_view"]/div[2]/div/div/div[2]/div[2]/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[3]/a')
#title = html.select('div.ct_list1 a.cb')

MAX = 31
for n in range(1, MAX, 10):
    raw = requests.get('https://www1.president.go.kr/petitions/?c=0&only=1&page='+str(n))
    html = BeautifulSoup(raw.text, "html.parser")

    petitions = petitions = html.select('div.ct_list1')

    for p in petitions:
            number = html.find_element_by_xpath('//*[@id="cont_view"]/div[2]/div/div/div[2]/div[2]/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[1]/span').text
            type = html.find_element_by_xpath('//*[@id="cont_view"]/div[2]/div/div/div[2]/div[2]/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[2]').text
            title = html.find_element_by_xpath('//*[@id="cont_view"]/div[2]/div/div/div[2]/div[2]/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[3]/a').text
            #title = p.select_one('div.ct_list1 a.cb').text


    print(number,type,title)

