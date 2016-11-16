#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import urllib2
from bs4 import BeautifulSoup
import sys

conf_file = 'conf_ircstats.yaml'
if os.path.isfile(conf_file):
    vars = yaml.load(open(conf_file))
else:
    raise StandardError(conf_file + " missing")

station_id = '10064349'
headtext = '<h2>Lämpötila Oulussa</h2> '

req = urllib2.Request('http://foreca.mobi/spot.php?l=' + station_id)
response = urllib2.urlopen(req)
html_doc = response.read()

soup = BeautifulSoup(html_doc, "lxml")
div = soup.find('div', id='cc')
div_inner = div.findAll('div', {'class': 'right'})
output_file = open(vars['header'], 'w')

output_file.write(headtext + str(div_inner[0]))
output_file.close()
