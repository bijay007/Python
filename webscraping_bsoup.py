import urllib
from BeautifulSoup import*

print 'TRY THIS:  http://python-data.dr-chuck.net/comments_297871.html'
url = raw_input('Enter domain name address..')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
summ = 0
count = 0

tags = soup('span')
for tag in tags:
    numm = int(tag.contents[0])
    summ = summ + numm
    count = count + 1
print 'Count', count
print 'Sum', summ
