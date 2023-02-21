import requests
from bs4 import BeautifulSoup

url = "https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=12607103&keywords=software+development&location=Manchester"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
companies = soup.find_all('div', class_="row businessCapsule--mainRow")

for company in companies:
    name = company.find('span', class_='businessCapsule--name').text.strip()
    website = company.find('a', class_='btn btn-yellow businessCapsule--ctaItem', href=True)['href']
    print(name, website)
