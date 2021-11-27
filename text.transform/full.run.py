
# Local modules
import github
import mdextension
import title

def full_run():
    github.clone()
    mdextension.rename_to_md_extension(limit=0)
    title.add_titles(limit=0)




if __name__ == '__main__':
    pass
    full_run()

    #mdextension.rename_to_md_extension(limit=0)
    #title.add_titles(limit=0)
