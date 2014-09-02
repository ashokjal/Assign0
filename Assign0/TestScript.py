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

def check_if_link_already_downloaded(href,urlDic):
	#print (urlDic.viewvalues())           		# print for Debug
	for url in urlDic.viewvalues():
		#print (href +' compared to '+ url)     # print for Debug
		if (href == url):
			return True
		elif (href == (url +'/')):
			return True
		elif (href+'/' == url):
			return True
	return False

def check_if_link_part_of_subdomain(href,urlDic):
	for url in urlDic.viewvalues():
		if url in href:
			return True
	return False	

#WebPagesDirectory.
path = r'WebPages'
urlDic = {} # used to store the dictionary of urls
if not os.path.isdir(path):
    os.makedirs(path)

# resquest for starting webpage.
url = raw_input("Enter a website to extract the URL's from: ")
count = 0
urlDic[str(count)+url] = 'http://' +url
r  = requests.get("http://" +url)



data = r.text
soup = BeautifulSoup(data)
for link in soup.find_all('a'):
    #print(link)                        # print for Debug
    hrefs = link.get('href')
    if 'http' not in hrefs:    		# if http not present dont ignore the href link.
	hrefs = "http://"+url+hrefs 
    # check if url already downloaded
    if check_if_link_already_downloaded(hrefs,urlDic): 
	print ('Old Link'+ hrefs)   	# print for Debug
        continue
    print ('New Link'+ hrefs)   	# print for Debug
    # check if link is in the same sub domain
    if not check_if_link_part_of_subdomain(hrefs,urlDic):
	print ('Link not in subdomain')
	continue
    # check if link is has key values.
    count = count+1
    urlDic[str(count)+url] = hrefs
    #print(hrefs, link.name)             # print for Debug
    save_to_file(str(count)+url, hrefs) 


#print (urlDic.keys())

keys = urlDic.viewkeys()
for k in keys:
	print (k , ' : ', urlDic[k])
	#pass


