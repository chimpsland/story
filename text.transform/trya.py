import re
import shlex  # for cmd string
import subprocess as sup

# for easy access during testing
import time
import datetime
import os

# Local
import tool
import config
import edit
import walk


file_path1 = './tmp/pink.world'
file_path2 = '/tmp/manssh'
file_path = '/tmp/story/mis/15k.txt.md'

#datetime.datetime.fromtimestamp(seconds)


rtitle = re.compile(r'^title\s*:', flags = re.I | re.M)
rdate = re.compile(r'^date\s*:', re.I)
rtags = re.compile(r'^tags\s*:', re.I)

t = os.path.getctime(file_path)


if __name__ == '__main__':
    pass



