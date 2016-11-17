#!/usr/bin/python
import os

scripts = [ 'add-dom.py',
            'foreca.py',
            'quotes.py',
          ]

for s in scripts:
    execfile('scripts/' + s)
    print '[Script] ' + s + ' executed'

