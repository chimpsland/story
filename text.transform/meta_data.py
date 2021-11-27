
# Local modules
import walk
import edit

def batch_insert_meta(limit=1):
    """
    rename utf-8 text files without markdown extension to file-name.md

    limit: is the number of files can be processed.
    """

    i = 0
    for fp in walk.get_files():
        print (i, fp)

        if edit.add_title(fp):
            i += 1

        if limit > 0:
            if( i == limit):
                break
