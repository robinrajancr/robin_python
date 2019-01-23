import urllib.request
import time
ts = time.time()
req = urllib.request.urlopen('http://www.youtube.com/')
pageHtml = req.read()
te = time.time()
print("Page Fetching Time : {} Seconds".format (te-ts))
