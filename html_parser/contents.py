import urllib.request
from bs4 import BeautifulSoup

url = "http://www.zdnet.co.kr/news/news_view.asp?artice_id=20181104031053&type=det&re=zdk"
#url = "https://en.wikipedia.org/wiki/Galaxy"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"})
page = urllib.request.urlopen(req)
the_page = page.read()#response.read()

soup = BeautifulSoup(the_page, 'html.parser')

textContent = []
for i in range(0, 20):
    paragraphs = soup.find_all("p")[i].text
    textContent.append(paragraphs)
# In my use case, I want to store the speech data I mentioned earlier.  so in this example, I loop through the paragraphs, and push them into an array so that I can manipulate and do fun stuff with the data.

#print(soup.prettify())
print(soup.find("div", {"id": "content"}))
