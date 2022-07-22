# -*- coding: utf-8 -*-
"""
@author: Uwe Ziegenhagen

"""

import os
import glob

os.chdir('./Codes') 

files = glob.glob('*.tex')

for file in files: # compile twice
    print(f'Running lualatex on {file} twice')

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
    os.system(f'magick -define colorspace:auto-grayscale=false {file} -background white -alpha remove -alpha off ../Pictures/{basename}.png')


with open('../README.md','w') as output:
    for pdf in glob.glob('*.pdf'):
        basename = pdf[:-4]
        title = basename.replace('-',' ')
        output.write(f'# {title}\r\n')

        if os.path.exists(f'../Annotations/{basename}.md'):
            with open(f'../Annotations/{basename}.md', "r") as f:
                annotation = f.read()
                output.write(f'\n{annotation}\n\n')                
        
        
        output.write('```latex\n')

        with open(f'{basename}.tex') as code:
            output.write(code.read())

        output.write('\n```\r\n')
        
        output.write(f'![{basename}](Pictures/{basename}.png)')
        output.write('\r\n')