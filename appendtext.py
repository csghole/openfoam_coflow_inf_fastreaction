#!/usr/bin/env python3
import os
file_list = os.listdir('system')
for file in file_list:
    with open(file, 'wt') as f:
        f.write('text\n')
