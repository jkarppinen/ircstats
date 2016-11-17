#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import os
import random
import sys
import urllib2
import yaml
import datetime

def add_carousel_item(content, active=False):

    html = '<div class="carousel-item">'
    if active:
        html = '<div class="carousel-item active">'
    html = html + content + '</div>'
    return html

conf_file = 'conf_ircstats.yaml'
if os.path.isfile(conf_file):
    vars = yaml.load(open(conf_file))
else:
    raise StandardError(conf_file + " missing")

quote = random.choice(vars['quotes'])

output_file = open(vars['header'], 'r+')
lines = output_file.readlines()
output_file.seek(0)
quote_html = """<div class="quote_container">
               <div class="quote">""" + quote['quote'] + """</div>
               <div class="quote_author"> - """ + quote['author'] + """</div>
       </div>"""
carousel_html = add_carousel_item(quote_html, True)

xmas_diff = datetime.date(2016,12,24) - datetime.date.today()

if (xmas_diff) >= datetime.timedelta(seconds=1):
    quote_html = """<div class="quote_container">
            <div class="quote">%s päivää jouluun!</div>
            """
    carousel_html = carousel_html + add_carousel_item(quote_html % str(xmas_diff.days), False).decode('utf-8').strip()

html = """
    <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
            """ + carousel_html + """
        </div>
    </div>
"""
print html
output_file.write(html.encode('utf-8'))
output_file.writelines(lines)
output_file.close()

