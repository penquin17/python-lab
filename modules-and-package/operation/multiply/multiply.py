from . import __get_path
import sys
sys.path.append(__get_path('../add'))


from add import add


def multiply(x: int, y: int):
    result = 0
    for _ in range(y):
        result = add(result, x)
    return result
