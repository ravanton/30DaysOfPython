# What is Web Scraping

# Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.
# Веб-скрапинг — это процесс извлечения и сбора данных с веб-сайтов и их хранения на локальном компьютере или в базе данных.

# Чтобы начать парсить сайты, вам нужны запросы , beautifoulSoup4 и сайт .

# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
# Let us declare url variable for the website which we are going to scrape.
url = 'https://archive.ics.uci.edu/ml/datasets.php'
# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)