#!/usr/bin/env/python
# Generates a README directory of the contents of the step subdirectories
# The links are correct only for the master branch

import glob

outfile = '../steps/README.md'
link_root = 'https://github.com/lsst-camera-dh/camera-eotest-configs/blob/master/steps/'

files = glob.glob('../steps/*/*.cfg') + glob.glob('../steps/*/*/*.cfg')
files.sort()

f = open(outfile,'w')

f.write('# Index of camera verification test configuration files\n')
print('# Index of camera verification test configuration files')
for file in files:
    entry = file.split('steps/')[1]
    entry_esc = entry.replace('_', '\_')
    f.write('* [' + entry_esc + '](' + link_root + entry + ')\n')
    print('* [' + entry_esc + '](' + link_root + entry + ')')

f.close()
