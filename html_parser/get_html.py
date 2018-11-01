#get html from a website

import urllib.request

#req = urllib2.Request('http://www.zdnet.co.kr/news/news_view.asp?artice_id=20180226164407')
#url = 'http://www.zdnet.co.kr/news/news_view.asp?artice_id=20180226164407'
url = "http://www.zdnet.co.kr"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
the_page = response.read()
print('here is the output : ')
print(the_page)

#2to3 tool converts sources