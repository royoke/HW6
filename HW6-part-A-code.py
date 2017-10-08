from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

sum_list = []
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
	sum_list.append(int(tag.contents[0]))

print(sum(sum_list))