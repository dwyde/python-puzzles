"""
A Python 2 puzzle: get the `type` object.

First I call `ast.literal_eval()` on your input. Then, if it looks good,
I call `eval()` on it.
"""
import ast


def pre_eval(value):
    """ Check the value before later calling `eval()` on it.
    """
    if isinstance(value, str):
        raise ValueError('No strings allowed!')
    if '(' in value:
        raise ValueError('No callable mischief allowed :-)')

def check_object(value):
    """ `eval()` a value, and see if it's the `type` object.
    """
    obj = eval(value, {'__builtins__': {}})
    if obj is type:
        print 'You win!'
    else:
        raise ValueError('That is not my type of object!')

def main():
    user_input = raw_input('Enter something that evals to the `type` object: ')
    value = ast.literal_eval(user_input)
    pre_eval(value)
    check_object(value)


if __name__ == '__main__':
    main()
