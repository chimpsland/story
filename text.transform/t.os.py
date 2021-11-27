
import magic
# from_file( file name)


standard_text = 'UTF-8 Unicode text'

# os.listdir()

#If you want just files, you could either filter this down using os.path:

from os import listdir
from os.path import isfile, join, abspath

mypath = './'
abs_cwd = abspath(mypath)

print(abs_cwd)

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

# # or you could use os.walk() which will yield two lists for each directory it visits - 
# # splitting into files and dirs for you. 
# # If you only want the top directory you can break the first time it yields
# 
# from os import walk
# 
# f = []
# for (dirpath, dirnames, filenames) in walk(mypath):
#     print('dirpath: ', dirpath)
#     f.extend(filenames)
#     break
# 
# # or, shorter:
# 
# from os import walk
# 
# filenames = next(walk(mypath), (None, None, []))[2]  # [] if no file
# 

