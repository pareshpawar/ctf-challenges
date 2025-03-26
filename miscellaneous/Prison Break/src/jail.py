#!/usr/bin/python

import sys

class Sandbox(object):
    def execute(self, code_string):
        exec(code_string)
        sys.stdout.flush()

sandbox = Sandbox()

_raw_input = raw_input

main = sys.modules["__main__"].__dict__
orig_builtins = main["__builtins__"].__dict__

builtins_whitelist = set((
    #exceptions
    'ArithmeticError', 'AssertionError', 'AttributeError', 'Exception',

    #constants
    'False', 'None', 'True',

    #types
    'basestring', 'bytearray', 'bytes', 'complex', 'dict',

    #functions
    'abs', 'bin', 'dir', 'help'

    # blocked: eval, execfile, exit, file, quit, reload, import, etc.
))

for builtin in orig_builtins.keys():
    if builtin not in builtins_whitelist:
        del orig_builtins[builtin]

print("Find the flag.")
sys.stdout.flush()

def flag_function():
    flag = "ctf7{pr1s0n_br34k_fr0m_th3_hic4th0n}"

while 1:
    try:
        sys.stdout.write(">>> ")
        sys.stdout.flush()
        code = _raw_input()
        sandbox.execute(code)

    except Exception:
        print("You have encountered an error.")
        sys.stdout.flush()
