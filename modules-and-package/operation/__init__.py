import os


def __get_pwd() -> str:
    return os.path.abspath(os.path.dirname(__file__))


def __get_path(rel_path: str) -> str:
    anchor = __get_pwd()
    path = os.path.join(anchor, rel_path)
    return path
