import webbrowser # web browser module to open websites

# list of urls: python
url_list = [
    'http://www.python.org',
    'http://www.youtube.com'
]
# opens the above list of websites in a defferrent tab
# for url in url_list:
#     webbrowser.open_new_tab(url)

import requests # importing the request module
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url)
print(response)
print(response.status_code)