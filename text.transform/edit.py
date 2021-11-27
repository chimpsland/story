import os
import datetime

import magic

# Local modules
import tool


def check_title(file_path):
    """
    return 'has title' if found

    no title, None, if not found
    file_path is full path with file name and extension
    """
    #print('is text file: ', tool.is_utf8_text_file(file_path))
    if tool.is_utf8_text_file(file_path):
        with open(file_path, 'r') as f:
            text = f.read()
            head = text[:300]

            if tool.has_title(head):
                return 'has title'
            else:
                return 'no title'

            pass
        pass
    return None


def check_title_in_text(text):
    """
    return 'has title' if found

    no title, None, if not found
    text: default to system utf-8
    """

    head = text[:300]

    if tool.has_title(head):
        return 'has title'
    else:
        return 'no title'


front_meta_str = """title: {title}
date: {date}

"""


def make_file_name_as_title(file_path):

    basename = os.path.basename(file_path)

    front_meta = "title: {name} \n\n".format(name = basename)

    return front_meta


def make_front_matter(abs_file_path):
    """

    abs_file_path: file name with abs full path

    """
    #make_file_name_as_title(abs_file_path)

    basename = os.path.basename(abs_file_path)

    ct = os.path.getctime(abs_file_path)
    t  = datetime.datetime.fromtimestamp(ct)
    iso_time_str = t.strftime('%Y-%m-%d %H:%M:%S')


    front_matter = front_meta_str.format(title=basename, date=iso_time_str)
    return front_matter


def insert_title_date(abs_file_path):
    """
    insert title and date, return True

    But for git, the file date changed to time of clone-ing,
    so the date is useless and confuse

    abs_file_path: file name with abs full path
    """
    # Only do ASCII or Unicode UTF-8 text file
    info = magic.from_file(abs_file_path)
    print('file info: ', info)
    go_ahead = (info.startswith('ASCII text') or
        info.startswith('UTF-8 Unicode text'))
    if not go_ahead:
        return info

    #ua = tool.utf8_or_ascii(abs_file_path)
    #if not ua:
    #    return False

    with open(abs_file_path, 'r+') as f:
        text = f.read()
        #print("\n{}\n".format(text[:100]))

        ct = check_title_in_text(text)
        print("check title result: ", ct)

        if check_title_in_text(text) == "has title":
            return False

        front_meta = make_front_matter(abs_file_path)
        print(front_meta)

        ta = front_meta + text

        f.seek(0)
        f.write(ta)

        # This should be only chance to return True
        return True


def insert_title(abs_file_path):
    """
    insert title only, return True on success.

    abs_file_path: file name with abs full path
    """
    # Only do ASCII or Unicode UTF-8 text file
    info = magic.from_file(abs_file_path)
    #print('file info: ', info)
    go_ahead = tool.utf8_or_ascii(abs_file_path)
    if not go_ahead:
        return info

    with open(abs_file_path, 'r+') as f:
        text = f.read()
        #print("\n{}\n".format(text[:100]))

        if check_title_in_text(text) == "has title":
            return False

        front_meta = make_file_name_as_title(abs_file_path)
        #print(front_meta)

        ta = front_meta + text

        f.seek(0)
        f.write(ta)

        # This should be only chance to return True
        return True


if __name__ == '__main__':
    pass

    #print('in file edit.py,   __name__ == "__main__"')
    #result = make_file_name_as_title(file_path)
    #print(result)

    file_path1 = '/tmp/story/mis/hk.wumao'
    file_path2 = '/tmp/story/mis/xi.top100'
    file_path = '/tmp/story/y10m/world.md'
    #insert_title_date(file_path)
    insert_title(file_path)

