#!/usr/bin/python
import glob
import os
import yaml


conf_file = 'conf_ircstats.yaml'
if os.path.isfile(conf_file):
    vars = yaml.load(open(conf_file))
else:
    raise StandardError(conf_file + ' missing. Did you run `python setup.py` ?')

print ' [  1/2] Generate pisg'
os.system('pisg --configfile=' + vars['pisg_config'])
print 'pisg file generated with --configfile=' + vars['pisg_config']
print ''

print '[   2/2] Run scripts'
for file in glob.glob('scripts/*.py'):
    execfile(file)
    print '[Script] ' + file + ' executed'

