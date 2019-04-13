import urllib2
import urllib

#request = urllib2.Request("http://www.baidu.com")
#response = urllib2.urlopen("http://www.baidu.com")
#response = urllib2.urlopen(request)

values = {"username":"windspears@163.com","password":"wind121200"}
data = urllib.urlencode(values)
url = "https://mail.163.com"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
