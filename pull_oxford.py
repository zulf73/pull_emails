
import re
import requests
from bs4 import BeautifulSoup as soup
from collections import deque
from HTMLParser import HTMLParser

#	new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
#	emails.update(new_emails)

h = HTMLParser()
def get_emails( url ):
	
	#print("Processing %s" % url)
	try:
    		response = requests.get(url)
		#new_emails = set(re.findall(r"mailto:([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)", response.text, re.I))
		new_emails0 = set( re.findall(r"<p class='email'><a\s+href=\"(&#109;.+)\"", response.text, re.I))
		new_emails =  set( [h.unescape(x) for x in new_emails0])
		return new_emails
	except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
	    # ignore pages with errors
 		pass
	

f = open('oxford_physics.html')
urls =  deque()
for line in f:
	m = re.findall( r'/contacts/people/(.+?)"', line, re.MULTILINE)
	for g in m:
		new_url = 'https://www2.physics.ox.ac.uk/contacts/people/'  + g
		urls.append( new_url)
for q in urls:
	ne = get_emails( q )
	for e in ne:
		print e





