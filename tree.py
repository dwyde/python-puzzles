"""
A Python 2 puzzle: understand a dumped Abstract Syntax Tree.

As in the other puzzles, your task is to supply the desired input.
"""
import ast


tree = """Module(body=[If(test=Compare(left=Call(func=Name(id='sum',
ctx=Load(), lineno=2, col_offset=3), args=[GeneratorExp(elt=
Call(func=Name(id='ord', ctx=Load(), lineno=2, col_offset=7),
args=[Name(id='char', ctx=Load(), lineno=2, col_offset=11)], keywords=[],
lineno=2, col_offset=7), generators=[comprehension(target=Name(id='char',
ctx=Store(), lineno=2, col_offset=21), iter=Call(func=Name(id='raw_input',
ctx=Load(), lineno=2, col_offset=29), args=[Str(s='> ', lineno=2,
col_offset=39)], keywords=[], lineno=2, col_offset=29), ifs=[])], lineno=2,
col_offset=7)], keywords=[], lineno=2, col_offset=3), ops=[Eq()],
comparators=[Num(n=1337, lineno=2, col_offset=49)], lineno=2, col_offset=3),
body=[Print(dest=None, values=[Str(s='You win!', lineno=3, col_offset=10)],
nl=True, lineno=3, col_offset=4)], orelse=[Raise(type=Call(func=Name(id=
'ValueError', ctx=Load(), lineno=5, col_offset=10), args=[Str(s='Bad value',
lineno=5, col_offset=21)], keywords=[], lineno=5, col_offset=10), inst=None,
tback=None, lineno=5, col_offset=4)], lineno=2, col_offset=0)])"""


def main():
    code_obj = compile(tree, '<ast>', 'eval')
    namespace = ast.__dict__.copy()
    compiled_ast = eval(code_obj, namespace)
    executable = compile(compiled_ast, '<code>', 'exec')
    exec executable


if __name__ == '__main__':
    main()
