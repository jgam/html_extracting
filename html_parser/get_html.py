#get html from a website

import urllib.request

#req = urllib2.Request('http://www.zdnet.co.kr/news/news_view.asp?artice_id=20180226164407')
#url = 'http://www.zdnet.co.kr/news/news_view.asp?artice_id=20180226164407'
url = "http://www.google.com"
#url = "http://www.zdnet.co.kr/news/news_view.asp?artice_id=20181104031053&type=det&re=zdk"
#url = "https://en.wikipedia.org/wiki/Galaxy"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"})
page = urllib.request.urlopen(req)
#request = urllib.request.Request(url)
#response = urllib.request.urlopen(request)
the_page = page.read()#response.read()
print('here is the output : ')
print(the_page)

#2to3 tool converts sources