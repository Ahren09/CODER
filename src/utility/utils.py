import os.path as osp

def check_cwd(fullpath):
    basename = osp.basename(osp.normpath(fullpath))
    assert basename.lower() in ["coder"], "Must run this file from parent directory (CODER/)"

