import webbrowser

# list of urls: python
url_list = [
    'http://www.python.org',
    'http://www.youtube.com'
]
# opens the above list of websites in a defferrent tab
for url in url_list:
    webbrowser.open_new_tab(url)