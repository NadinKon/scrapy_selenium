import json
from time import sleep
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


s = Service('C:\\Users\\Nadin\PycharmProjects\Sele\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'https://www.govassociation.org/directory'
driver.get(url)
sleep(5)
soup = BeautifulSoup(driver.page_source, 'lxml')
f = soup.find_all('a', title="Go to member details")

resultat = []
spisok_urls = []
for i in f:
    spisok_urls.append(i.get('href'))

company = []
phone = []
mail = []
for link in spisok_urls:
    response = requests.get(url=link)
    so = BeautifulSoup(response.text, 'lxml')
    try:
        comp = so.find('span', id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl02_TextBoxLabel2999526").text
        phon = so.find('span', id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl04_TextBoxLabel2999528").text
        mai = so.find('span', id="FunctionalBlock1_ctl00_ctl00_memberProfile_MemberForm_memberFormRepeater_ctl03_TextBoxLabel2999523").text
    except Exception as j:
        comp = None
        phon = None
        mai = None
    company.append(comp)
    phone.append(phon)
    mail.append(mai)

resultat = list(zip(company, phone, mail))

with open('res.json', 'w') as file:
    json.dump(resultat, file, indent=4)






