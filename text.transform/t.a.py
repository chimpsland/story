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

#t = os.path.getctime(file_path)


def test_check_title():
    fp = '/tmp/story/21/story.y21.m2.d16.txt.md'

    with open(fp, 'r+') as f:
        text = f.read()
        print("\n{}\n".format(text[:100]))

        ct = check_title_in_text(text)
        print("check title result: ", ct)

        if check_title_in_text(text) == "has title":
            return

        front_meta = make_front_matter(abs_file_path)
        print(front_meta)

        f.seek(0)

        ta = front_meta + text

        f.write(ta)



if __name__ == '__main__':
    pass
    #print('__name__ == "__main__"')
    #result = edit.check_title(file_path)
    #print(result)

    ##edit.insert_title(file_path)
    #fm = edit.make_front_matter(file_path)
    #print (fm)


    test_add_titles(0)



