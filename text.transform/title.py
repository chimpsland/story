
# Local modules
import walk
import edit


def add_titles(limit=1):
    """
    rename text files without markdown extension to file-name.md

    limit: is the number of files to be processed, 0 means no limit.
    """

    i = 0
    for fp in walk.files_need_change():

        if edit.insert_title(fp) == True:
            i += 1
            print (i, fp)

        if limit > 0:
            if( i == limit):
                break



if __name__ == '__main__':
    pass
    #print('__name__ == "__main__"')
    #result = edit.check_title(file_path)
    #print(result)

    ##edit.insert_title(file_path)
    #fm = edit.make_front_matter(file_path)
    #print (fm)


    add_titles(0)

