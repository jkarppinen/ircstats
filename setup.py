#!/usr/bin/python

from shutil import copyfile
import glob
import os
import yaml

def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)

print 'Creating configuration files...'
for file in os.listdir('defaults'):
    if not os.path.isfile(file):
        copyfile('defaults/' + file, file)
        print '[     New] Config file ' + file
    else:
        print '[Existing] Config file ' + file

print ''
print 'Configuration files created succesfully'
print ''

conf_file = 'conf_ircstats.yaml'
if os.path.isfile(conf_file):
    vars = yaml.load(open(conf_file))
else:
    print '[ Error] '+ conf_file + ' missing. Did you run `python setup.py` ?'

print 'Creating dummy pages if not existing...'
pages = [vars['header'], vars['footer'], vars['stats']]


for file in pages:
    try:
        os.stat(os.path.dirname(file))
    except:
        os.mkdir(os.path.dirname(file))

    print 'Touching file ' + file
    touch(file)

print 'Pages created successfully'


