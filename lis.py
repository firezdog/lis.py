import math
import operator as op

Symbol = str # A Symbol is a string.
Number = (int, float) # A Number is an int or a float.
Atom = (Symbol, Number) # An Atom is a symbol or a number.
List = list # A List is a list.
Exp = (Atom, List) # An Exp is an Atom or a List.

def tokenize (chars: str) -> List:
    "Lexical analysis: convert a string of characters into a list of tokens using split()."
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program: str) -> Exp:
    "tokenize() string and read_from_tokens() to generate tree."
    output = read_from_tokens_recursively(tokenize(program), [])
    return output[0]

def read_from_tokens_recursively(tokens: List, E: List) -> Exp:
    if len(tokens) == 0:
        return E
    token = tokens.pop(0)
    if token == "(":
        E.append(read_from_tokens_recursively(tokens, []))
        return read_from_tokens_recursively(tokens, E)
    elif token == ")":
        return E
    else:
        E.append(int_or_not(token))    
        return read_from_tokens_recursively(tokens, E)

def read_from_tokens(tokens: list) -> Exp:
    "convert a string into a tree-like expression"
    if len(tokens) == 0:
        raise SyntaxError("Unexpected EOF")
    token = tokens.pop(0)
    if token == "(":
        E = []
        try:
            while tokens[0] != ")":
                E.append(read_from_tokens(tokens))
        except:
            # if there's no closing parenthesis, while never terminates and tokens has no 0 index.
            raise SyntaxError("No closing parenthesis.")
        # if this isn't here, program terminates on first close paren it encounters ???
        tokens.pop(0)
        return E
    elif token == ")":
        raise SyntaxError("Unexpected close parenthesis")
    else:
        return int_or_not(token)

def int_or_not(token: str) -> Atom:
    # first try to convert token to int, failing that float, failing that string
    try:
        return int(token)
    except:
        return float_or_sym(token)

def float_or_sym(token):
    try:
        return float(token)
    except:
        return Symbol(token)

# we use a dictionary to interpret symbols
def standard_env():
    env = {}
    env.update(vars(math))
    env.update({
        # mathematical operators
        '+': op.add, 
        '-': op.sub, 
        '*': op.mul, 
        '/': op.truediv, 
        '%': op.mod, 
        '>': op.gt, 
        '>=': op.ge, 
        '<=': op.le,
        '=': op.eq,
        'user_defined': {}
    })
    return env

global_env = standard_env()

def eval(x: Exp, env=global_env) -> Exp:
    "Evaluate an expression in an environment."
    if isinstance(x, Number):
        return x
    elif isinstance(x, Symbol):
        if x in env:
            return env[x] 
        elif x in env['user_defined']:
            return eval(x, env['user_defined'])
        else:
            return x
    elif x[0] == 'define':
        # remember, x should be a triple consisting of 'define', a symbol, and an expression
        # so we throw away 'define' and set the value for env[<symbol>] = eval(expression).
        # original solution has the disadvantage that it allows the user to define away things like '+' --
        # so I put the symbol in a user dictionary where namespace collisions can do no harm.
        # downside -- user enters 'user_defined' as a symbol...
        (_, definiendum, exp) = x
        definiens = eval(exp, env)
        env['user_defined'][definiendum] = definiens
        return "{} = {}".format(definiendum, definiens)
    elif x[0] == 'if':
        (_, condition, consequence, alternative) = x
        result = consequence if eval(condition, env) else alternative
        return eval(result, env)
    else:
        # the first entry in the list is one of our functions
        func = eval(x[0], env)
        # evaluate everything else
        args = [eval(arg, env) for arg in x[1:]]
        # this all assumes well-formed input
        return func(*args)

# REPL
while True:
    entry = input("lispy> ")
    try:
        print(eval(parse(entry)))
    except:
        print("Error: malformed input!")