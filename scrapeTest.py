import urllib2
from bs4 import BeautifulSoup

urls = ['http://www.eppingclub.com/category/entertainment-weekly/']

for url in urls:
    output = urllib2.urlopen(url)
    html = output.read()
    soup = BeautifulSoup(html)
    link_data = soup.findAll("div", {"class": "post-image-r"})
    # ext = re.findall('', str(link_data))
    for div in link_data:
        title = div.h2.a.string
        details = div.p.string
        #title = event_header.a.string
        #details = event_details.string
        print "Event name: %s \tEvent details: %s" % (title, details)



#soup = BeautifulSoup(urllib2.urlopen(
#'http://www.eppingclub.com/category/entertainment-weekly/').read())

#for row in soup('div', {'class': 'post-image-r'})[0]:
    #event = row('h2')
    #details = row('p')
    #print event.string, details.string