try:
    import sys

    from . import __get_path

    sys.path.append(__get_path('../add'))
    from add import add
except Exception as e:
    raise e


def multiply(x: int, y: int):
    result = 0
    for _ in range(y):
        result = add(result, x)
    return result
