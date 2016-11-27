#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import datetime
import urllib2
from bs4 import BeautifulSoup
import sys
import os
import yaml

conf_file = 'conf_ircstats.yaml'
if os.path.isfile(conf_file):
    vars = yaml.load(open(conf_file))
else:
    raise StandardError(conf_file + " missing")

station_id = '100643492'
headtext = '<h2>Lämpötila Oulussa</h2> '

req = urllib2.Request('http://foreca.mobi/spot.php?l=' + station_id)
response = urllib2.urlopen(req)
html_doc = response.read()

soup = BeautifulSoup(html_doc, "lxml")

# Find temperature
div = soup.find('div', id='cc')
temperature_div = div.findAll('div', {'class': 'right'})

# Find sunrise, sunset
div = soup.findAll('div', {'class': 'hourlyfc'})
sunrise_row = div[0].findAll('div', {'class': 'timecol'})[0].findAll('p')
sunset_row = div[1].findAll('div', {'class': 'timecol'})[0].findAll('p')

sunrise_time_data = sunrise_row[1].decode_contents(formatter="html")
sunset_time_data = sunset_row[1].decode_contents(formatter="html")

# Convert into datetime objects
now = datetime.datetime.now()
sunrise_time = datetime.datetime.strptime(sunrise_time_data, '%H:%M')
sunrise_time = now.replace(hour=sunrise_time.hour, minute=sunrise_time.minute)
sunset_time = datetime.datetime.strptime(sunset_time_data, '%H:%M')
sunset_time = now.replace(hour=sunset_time.hour, minute=sunset_time.minute)

print sunrise_time, sunset_time, now > sunrise_time
if now < sunrise_time:
    sun_status = 'Aurinko nousee ' + str(sunrise_time.hour) + ':' + str(sunrise_time.minute)
elif now > sunrise_time and now < sunset_time:
    sun_status = 'Pimeys laskeutuu n. ' + str(sunset_time.hour) + ':' + str(sunset_time.minute)
else:
    sun_status = 'Pimeys on laskeutunut ' + str(sunset_time.hour) + ':' + str(sunset_time.minute)

sun_status = '<div class="sun_status">' + sun_status + '</div>'
output_file = open(vars['header'], 'w')
output_file.write(headtext + str(temperature_div[0]) + str(sun_status))
output_file.close()
