# html_extracting
html_extracting before machine learning

Set up the git environment so to follow easily libraries&&packages and codes

Python 3.5.2 installation
1. zlib error
=> manually downloaded zlib.tar and ./configure, make, and make install because of 'Mojave'

Setting up the virtualenv
pyenv versions -> to check the available python versions
pyenv virtualenv 3.5.2 htmlEX -> create python Version 3.5.2 and call it htmlEx
pyenv activate htmlEx -> select htmlEx as an environment
pyenv global htmlEx -> set this environment as global environment

Installing tools
1. go into a given URL and get HTML for website
-> https://docs.python.org/2/howto/urllib2.html
2.html parsing
-> https://docs.python.org/3/library/html.parser.html

3. get_html.py
-> using urllib to get the page of url and save it to some variables

4. bsoup.py
-> basic check installation of beautifulsoup and see if it actually works
-> need to implement this with #3 so that I can combine the two functionalities together

5. contents.py
-> combining #3 & #4. Now able to scrape Korean webiste and contents only.

6. Konlpy
-> installed Konlpy by doing : pip3 install konlpy
***Make sure to use pip3, NOT pip!***

7. outputs
-> outputs are saved as outputs. I was able to differentiate noun(?) using the tools but not sure.


Tomorrow Task:
-dragnet required how to use! (don't need but still need to look at it!)

setting up the local environment
