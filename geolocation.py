import re
import sys
import urllib2
import json
from bs4 import BeautifulSoup

usage = "Run format: geolocation.py IPAddress"

if len(sys.argv)!=2:
    print(usage)
    sys.exit(0)

if len(sys.argv) > 1:
    ipaddr = sys.argv[1]

geody = "http://ip-api.com/json/" + ipaddr
html_page = urllib2.urlopen(geody).read()
soup = BeautifulSoup(html_page, "html.parser")
json_string = soup.encode('utf-8')
jsondata = json.loads(json_string)

print "\n" + "City: " + jsondata["city"] + "\n"
print "Zip: " + jsondata["zip"] + "\n"
print "Country: " + jsondata["country"] + "\n"
print "Region: " + jsondata["regionName"] + "\n"
print "ISP: " + jsondata["isp"] + "\n"
print "Company: " + jsondata["as"] + "\n"
print "Timezone: " + jsondata["timezone"] + "\n"
print "Longitude: " + str(jsondata["lon"]) + "\n"
print "Latitude: " + str(jsondata["lat"]) + "\n"