import subprocess
import shlex

# Local modules
import tool
import config


def clone():
    """
    clone the repository in config.py
    remove dir if exists before-hand
    """

    tool.rm_if_exists(config.local_repo_path)

    clone_cmd = " ".join([
        "git clone",
        config.story_git,
        config.local_repo_path
        ])

    cmd_list = shlex.split(clone_cmd)
    print(cmd_list)

    result = subprocess.run(cmd_list, capture_output=True)
    print(result)


def pull():
    """
    git pull the repository in config.py
    """
    pull_cmd = "git pull"

    result = subprocess.run(
            shlex.split(pull_cmd),
            cwd = config.local_repo_path,
            capture_output=True)

    if result.returncode == 0:
        print(config.local_repo_path, 'pulled sucessful')
    print(result)


if __name__ == "__main__":
    clone()
