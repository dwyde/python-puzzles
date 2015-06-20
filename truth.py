"""
A Python 2 puzzle: find a Python expression that meets certain constraints.
"""
import ast
import __builtin__


class CallVisitor(ast.NodeVisitor):
    """ Count the number of `Call` nodes in an AST.
    """
    def __init__(self, *args, **kwargs):
        super(CallVisitor, self).__init__(*args, **kwargs)
        self.call_count = 0

    def visit_Call(self, node):
        self.call_count += 1
        self.generic_visit(node)

def check_ast(value):
    """ Check if an ast is dangerous, before eval()'ing it.

    I think that you need two Call nodes to do damage when
    eval()'ing without built-ins: one to get something dangerous,
    and one to call it. I'd love to be shown otherwise :-)
    
    For more details, please see
    http://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html
    """
    visitor = CallVisitor()
    tree = ast.parse(value, '<user>', 'eval')
    visitor.visit(tree)
    if visitor.call_count > 1:
        raise ValueError('Only one Call node allowed!')

def construct(value):
    """ Call eval() on user input, without built-ins in the namespace.

    Raise an error if the value is a built-in object, or if
    the result of calling the object is truthy.
    """
    constructor = eval(value, {'__builtins__': {}})
    obj = constructor()
    if obj.__class__ in __builtin__.__dict__.values():
        raise ValueError('No built-ins, please!')
    elif obj:
        raise ValueError('I want to initialize something false.')
    else:
        print 'You win!'

def main():
    value = raw_input('Give me a special value: ')
    check_ast(value)
    construct(value)


if __name__ == '__main__':
    main()
