"""Clone GitHub repositories

Run `pip install gitpython` to install the gitpython package.

Then run this script using CODER/ as the current working directory.

"""

import os
import os.path as osp
from git import Repo

from utility.utils import check_cwd

check_cwd(os.getcwd())

# Assume you have untar the stargazers.tar.gz file under ../data/stargazers
DATA_DIR = '../data'

os.makedirs(osp.join(DATA_DIR, 'repositories'), exist_ok=True)

for repo_owner in os.listdir(osp.join(DATA_DIR, 'stargazers')):
    for repo_name in os.listdir(osp.join(DATA_DIR, 'stargazers', repo_owner)):
        repo_path = osp.join(DATA_DIR, 'repositories', repo_owner, repo_name)
        if osp.exists(repo_path):
            continue

        repo_url = f"https://github.com/{repo_owner}/{repo_name}.git"

        try:
            Repo.clone_from(repo_url, repo_path)

        except Exception as e:
            print(f"Fail to clone: {repo_owner}/{repo_name}: {e}")

