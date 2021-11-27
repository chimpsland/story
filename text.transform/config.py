import os.path

story_git = "git@github.com:goodagood/story.git"
story_git_https = "https://github.com/goodagood/story.git"

repo_name = "story"
tmp_dir = "/tmp/"
local_repo_path = os.path.join(tmp_dir, repo_name)


exclude_files = ['Makefile', 'LICENSE' ]
# dot files, ie. .* any file start from dot/.

exclude_extensions = ['.js', '.json', '.html', '.htm','.py',  '.pyc',
        '.yml', '.yaml', '.xml', '.css', '.sass', '.scss', '.c', '.cpp',
        '.php', '.java', '.rb', '.sh']


# only dirs in this list
# This is for `story` repo
include_dirs = [
        '21',
        'chimpsland',
        'dignity.death',
        'mis',
        'revolve',
        'team5',
        'y10m',
        ]

# Every file within this folder would be ignored
# dirs: bak
exclude_dirs = [ '.git', 'docs', 'img', 'images', 'js', 'style', 'output']

