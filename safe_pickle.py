"""
A Python 2 puzzle: use pickle to create a happy object.

Specifically, your pickle payload should create an object that takes a `happy`
keyword argument to its constructor, then sets an attribute of the same name.

You should be able to pipe input in, or press `Ctrl+d` to send EOF.

No credit will be awarded for merely running code via pickle!
This is a puzzle, not a realistic situation :-)
"""
import pickle
import pickletools
import sys


def check_opcodes(pickle_data):
    """ Blacklist pickle opcodes that would make this too easy.
    """
    banned_opcodes = set([pickle.STRING, pickle.INST, pickle.REDUCE])
    for opcode, args, _ in pickletools.genops(pickle_data):
        if opcode.code in banned_opcodes:
            raise ValueError('Opcode not allowed: "%s".' % opcode.name)

def load_payload(pickle_data):
    """ Load the pickle data, and check its "happy" attribute.
    """
    obj = pickle.loads(pickle_data)
    result = obj(happy=True)
    if result.happy is True:
        print 'You win!'
    else:
        raise ValueError('Unhappy object :-(')

def main():
    print 'Please provide a pickled payload: '
    pickle_data = sys.stdin.read()
    check_opcodes(pickle_data)
    load_payload(pickle_data)


if __name__ == '__main__':
    main()
