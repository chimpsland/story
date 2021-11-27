import shutil

# local modules
import tool
import walk


def add_md_ext(file_path):
    """rename the file to add markdown extension: .md
    """
    if tool.has_markdown_ext(file_path):
        print( file_path, ' has markdown extension. ')
        return False
    else:
        md_ext = file_path + '.md'

        shutil.move(file_path, md_ext)
        print('{} rename to: {}'.format(file_path, md_ext))
        return md_ext



def rename_to_md_extension(limit=0):
    """
    rename utf-8 text files without markdown extension to file-name.md

    limit: is the number of files can be processed.
    """

    i = 0
    for fp in walk.files_need_change():
        has_ext = tool.has_markdown_ext(fp)

        # do the rename
        if add_md_ext(fp):
            i += 1
        if limit > 0:
            if( i == limit):
                break



if __name__ == '__main__':
    pass

    rename_to_md_extension(0)

