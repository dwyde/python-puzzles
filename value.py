"""
A Python 2 puzzle: get a value out of an inner function.

No opening parentheses are allowed: I hope you won't abuse `eval()` :-)
"""

def func(secret):
    def inner(value):
        return value is secret
    return inner
func = func(object())

def eval_and_check(user_input):
    """ Call `eval()` on user input, and run it through `func()`.

    If your value matches the secret inner value, you win!
    """
    value = eval(user_input)
    if func(value) is True:
        print 'You win!'
    else:
        raise ValueError('Wrong value.')

def main():
    user_input = raw_input('What is the secret value? ')
    if '(' in user_input:
        raise ValueError('I do not like parentheses.')
    eval_and_check(user_input)

if __name__ == '__main__':
    main()
