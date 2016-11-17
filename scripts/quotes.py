#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import os
import random
import sys
import urllib2
import yaml

conf_file = 'conf_ircstats.yaml'
if os.path.isfile(conf_file):
    vars = yaml.load(open(conf_file))
else:
    raise StandardError(conf_file + " missing")

quote = random.choice(vars['quotes'])

output_file = open(vars['header'], 'r+')
lines = output_file.readlines()
output_file.seek(0)
html = """<div class="quote_container">
               <div class="quote">""" + quote['quote'] + """</div>
               <div class="quote_author"> - """ + quote['author'] + """</div>
       </div>"""
output_file.write(html.encode('utf-8'))
output_file.writelines(lines)
output_file.close()

