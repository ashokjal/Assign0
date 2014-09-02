from bs4 import BeautifulSoup
import requests
import os
import urllib2

def save_to_file(filename,url):
	f = file(path+'/'+filename,'w')
	r = urllib2.urlopen(url)
	f.write(r.read())
	f.flush()
	f.close()



#WebPagesDirectory.
path = r'WebPages'
urlDic = {} # used to store the dictionary of urls
if not os.path.isdir(path):
    os.makedirs(path)

# resquest for starting webpage.
url = raw_input("Enter a website to extract the URL's from: ")
count = 0
urlDic[str(count)+url] = url
r  = requests.get("http://" +url)



data = r.text
soup = BeautifulSoup(data)
for link in soup.find_all('a'):
    #print(link)                        # print for Debug
    hrefs = link.get('href')
    if 'http' not in hrefs:    # if http not present dont ignore the href link.
	hrefs = "http://"+url+hrefs 
    # check if url already downloaded
    # check if link is in the same sub domain
    # check if link is has key values.
    count = count+1
    urlDic[str(count)+url] = hrefs
    print(hrefs, link.name)             # print for Debug
    save_to_file(str(count)+url, hrefs) 


#print (urlDic.keys())

keys = urlDic.viewkeys()
for k in keys:
	print (k , ' : ', urlDic[k])



