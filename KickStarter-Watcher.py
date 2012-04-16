# Bernard Roth
# 16 April 2012

import urllib2
# import re
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://www.kickstarter.com/projects/1613260297/shadowrun-returns').read())
project = soup.find('div', attrs={'class': 'NS-project_-running_board'})
# print project

z=1
h1s = soup.findAll('h1')
for h1 in h1s[1:2]:
 title = h1.contents[0].string
 print title

# Make a countdown clock
# 
# <h5 class="ksr_page_timer" data-end_time="Sun, 29 Apr 2012 02:59:00 -0400">
# <div class="num">&nbsp;</div>
# <span class="text">&nbsp;</span>
# </h5>
# <div id="banner">
# This project will be funded on Sunday Apr 29,  2:59am EDT.
# </div>

maindiv = soup.find('div', attrs={'class': 'NS-projects-ecom'})
# print maindiv

numdiv = soup.findAll("div", {"class": "num"})
# print numdiv

i = 1
for tag in numdiv:
 num=tag.find(text=True)
 # print i, num
 if i == 1:
     print 'Backers: ', num
 elif i == 2:
     print 'Pledged: ', num
 elif i==2:
     break
 # print num
 i += 1
