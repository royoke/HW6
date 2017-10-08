from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))


for num in range(count+1):
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	url_list = []
	print ("Retreiving: ", url)
	tags = soup('a')
	for tag in tags:
		url_list.append(tag.get('href', None))
	url = url_list[position - 1]
	



