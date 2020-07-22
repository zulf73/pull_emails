
import re
import requests
from bs4 import BeautifulSoup as soup
from collections import deque
import wget
#	new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
#	emails.update(new_emails)


def get_emails(url):
    #print("Processing %s" % url)
    try:
        #filename = wget.download(url)
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        text = response.text
        # print response.text
        # print filename
        #text = open(filename).read()
        new_emails = set(re.findall(
            r"mailto:([A-Za-z0-9\.\-+_]+@[A-Za-z0-9\.\-+_]+\.[a-z]+)", text, re.I))
        # print new_emails
        return new_emails
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        # ignore pages with errors
        pass


f = open('berk_bus.html')
urls = deque()
# print get_emails('https://haas.berkeley.edu/faculty/anderson-cameron/')

for line in f:
    m = re.findall(r'faculty/(.+?)"', line, re.MULTILINE)
    for g in m:
        # print g
        new_url = 'https://haas.berkeley.edu/faculty/' + g
        urls.append(new_url)
for q in urls:
    # print q
    ne = get_emails(q)
    for e in ne:
        print e
