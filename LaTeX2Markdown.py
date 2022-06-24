# -*- coding: utf-8 -*-
"""
@author: Uwe Ziegenhagen

"""

import os
import glob

files = glob.glob('*.tex')

for file in files: # compile twice
    print(file)    
    os.system(f'lualatex -interaction=batchmode {file}')
    os.system(f'lualatex -interaction=batchmode {file}')

# Remove files that are not required
files_to_delete = ['log', 'toc', 'aux', 'nav', 'snm', 'out']
for filetype in files_to_delete:
    filelist = glob.glob(f'*.{filetype}')
    for f in filelist:
        os.remove(f)
        

for file in glob.glob('*.pdf'): # compile twice
    print(file)

    basename = file[:-4]
    os.system(f'magick -define colorspace:auto-grayscale=false {file} Pictures/{basename}.png')


with open('README.md','w') as output:
    for pdf in glob.glob('*.pdf'):
        basename = pdf[:-4]
        output.write(f'{basename}\r\n')
        
        output.write('```latex\r\n')

        with open(f'{basename}.tex') as code:
            output.write(code.read())

        output.write('\r\n```\r\n')
        
        output.write(f'![{basename}](Pictures/{basename}.png)')
        output.write('\r\n')