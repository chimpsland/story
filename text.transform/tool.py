
import re
import os.path
import shutil
import magic

# Local module
import config


def is_utf8_text_file(file_path):
    info = magic.from_file(file_path)
    return info.startswith('UTF-8 Unicode text')


def is_ascii_text_file(file_path):
    info = magic.from_file(file_path)
    return info.startswith('ASCII text')


def utf8_or_ascii(file_path):
    info = magic.from_file(file_path)
    go_ahead = (info.startswith('ASCII text') or
        info.startswith('UTF-8 Unicode text'))
    return go_ahead


rtitle = re.compile(r'^title\s*:', flags = re.I | re.M)
rdate = re.compile(r'^date\s*:',  flags = re.I | re.M)
rtags = re.compile(r'^tags\s*:',  flags = re.I | re.M)

def has_title(text):
    finds = rtitle.findall(text)
    num = len(finds)
    if num == 0:
        return False
    else:
        return True


def rm_if_exists(abs_path):
    if os.path.exists(abs_path):
        print('Remove: ', abs_path)
        shutil.rmtree(abs_path, ignore_errors=True)

def in_exclude_dirs(abs_path):
    path, file = os.path.split(abs_path)
    parts = path.split(os.path.sep)
    for dir in config.exclude_dirs:
        if dir in parts:
            return True
    return False


def should_exclude(abs_path):
    """exclude dot files, and more:
    files with extensions specified in config,
    certain names specified in config.
    """
    basename = os.path.basename(abs_path)

    if basename.startswith('.'):
        return True

    for ef in config.exclude_files:
        if ef == basename:
            return True

    name, ext = os.path.splitext(basename)
    for eext in config.exclude_extensions:
        if eext == ext:
            return True

    if in_exclude_dirs(abs_path):
        return True

    return False


def has_markdown_ext(file_path):
    name, ext = os.path.splitext(file_path)
    if ext.lower() in ['.md', '.mkd', '.markdown']:
        return True

    return False



if __name__ == "__main__":
    #file_path = "/tmp/manssh"
    #file_path = "/tmp/story/LICENSE"
    #file_path = "/tmp/story/LICENSE.py"

    #res = should_exclude(file_path)
    #print(res)
    pass

