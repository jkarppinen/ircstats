#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import datetime
import urllib2
import json
import requests
from bs4 import BeautifulSoup
import sys
import os
import yaml

conf_file = 'conf_ircstats.yaml'
if os.path.isfile(conf_file):
    vars = yaml.load(open(conf_file))
else:
    raise StandardError(conf_file + " missing")

url = 'http://api.openweathermap.org/data/2.5/weather'
params = dict(
            appid=vars['owm_api'],
            lang='fi',
            units='metric',
            q='Oulu,FI',
        )
response = requests.get(url=url, params=params)
data = json.loads(response.text)
headtext = '<h2>Sää Oulussa</h2>'

temp = data['main']['temp']
sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
now = datetime.datetime.now()

if (now - sunrise).total_seconds() > 0:
    sun_status = 'Aurinko nousee ' + str(sunrise.hour) + ':' + str(sunrise.minute)
elif (now - sunrise).total_seconds() < 0 and (now - sunset).total_seconds > 0:
    sun_status = 'Pimeys laskeutuu n. ' + str(sunset.hour) + ':' + str(sunset.minute)
else:
    sun_status = 'Pimeys on laskeutunut ' + str(sunset.hour) + ':' + str(sunset.minute)

weather_icon_img = '<div class="weather_icon"><img src="http://openweathermap.org/img/w/%s.png"></img></div>' % data['weather'][0]['icon']
temp_text = "<p>Lämpötila: %s &deg;C  %s</p>" % (temp, str(weather_icon_img))
sun_text = "<div class='sun_status'>%s</div>" % sun_status

output_file = open(vars['header'], 'w')
output_file.write(headtext + temp_text + sun_text)
output_file.close()
