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

    carousel_div = '<div class="carousel-item">'
    if active:
        carousel_div = '<div class="carousel-item active">'
    html = carousel_div + content + '</div></div>'
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
                   <div class="quote">%s</div>
                   <div class="quote_author"> - %s</div>
               </div>
               """ % (quote['quote'], quote['author'])

carousel_html = add_carousel_item(quote_html, True)

xmas_diff = datetime.date(2016,12,24) - datetime.date.today()

if (xmas_diff) >= datetime.timedelta(seconds=1):
    quote_html = """
        <div class="quote_container">
            <div class="quote">%s päivää jouluun!</div>
        </div>""" % str(xmas_diff.days)

    carousel_html = carousel_html + add_carousel_item(quote_html, False).decode('utf-8').strip()

html = """
    <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">%s</div>
    </div>""" % (carousel_html)

output_file.write(html.encode('utf-8'))
output_file.writelines(lines)
output_file.close()

