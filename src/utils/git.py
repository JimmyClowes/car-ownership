import git

def get_root(path='.'):
    """
    Get path of top level git repo from input path.

    Args:
        path (str, optional): Path from which to find
        top level git repo. Defaults to '.'.
    """
    git_repo = git.Repo(path, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")
    return(git_root)