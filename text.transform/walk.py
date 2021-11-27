#!python

import os

# local modules
import tool
import config
import edit


#test_dir = '.'
test_dir = config.local_repo_path



## traverse root directory, and list directories as dirs and files as files
#for root, dirs, files in os.walk(test_dir):
#    path = root.split(os.sep)
#    print((len(path) - 1) * '---', os.path.basename(root))
#    for file in files:
#        print(len(path) * '---', file)
#

def finding():
    # for think stage

    i = 0
    for root, dirs, files in os.walk(test_dir, followlinks=True):
        #print(root, dirs)
        type(dirs)
        type(files)

        if (i > 10):
            break

        for file in files:
            print(i) #empty line

            file_path = os.path.join(root, file)
            print(file_path)
            print('is text file: ', tool.is_utf8_text_file(file_path))

            titled = edit.check_title(file_path)
            print(titled)


            i = i + 1
            if (i > 10):
                break



def abs_path_text_files():
    """test stage
    """
    for root, dirs, files in os.walk(test_dir, followlinks=True):

        for file in files:

            file_path = os.path.join(root, file)
            print(file_path)
            is_utf8_unicode_text = tool.is_utf8_text_file(file_path)
            print('is utf-8 text file: ', is_utf8_unicode_text)

            if is_utf8_unicode_text:
                titled = edit.check_title(file_path)
                print('title: ', titled)
                if titled != 'has title':
                    yield file_path


def get_files():
    """
    walk into story folders recursivly, give files should be processed
    """

    for dir in config.include_dirs:
        absdir = os.path.join(config.local_repo_path, dir)
        #print(absdir)

        for root, dirs, files in os.walk(absdir):
            for file in files:
                file_path = os.path.join(root, file)
                #print(file_path)

                if tool.should_exclude(file_path):
                    continue # go to next loop

                if tool.utf8_or_ascii(file_path):
                    yield file_path
                    # process the file
                    #if edit.check_title(file_path):


def files_need_change():
    """
    walk into story folders recursivly, give files should be processed

    2021-11-16
    """
    for root, dirs, files in os.walk(config.local_repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            #print(file_path)

            if tool.should_exclude(file_path):
                continue # go to next loop

            if tool.utf8_or_ascii(file_path):
                yield file_path

    #for dir in config.include_dirs:
    #    absdir = os.path.join(config.local_repo_path, dir)
    #    #print(absdir)

    #    for root, dirs, files in os.walk(absdir):
    #        for file in files:
    #            file_path = os.path.join(root, file)
    #            #print(file_path)

    #            if tool.should_exclude(file_path):
    #                continue # go to next loop

    #            if tool.utf8_or_ascii(file_path):
    #                yield file_path



if __name__ == "__main__":
    for index, file_path in enumerate(abs_path_text_files()):
        print (index, file_path)
        if(index > 2):
            break




