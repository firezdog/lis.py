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
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list, E=[], level=0) -> Exp:
    "convert a string into a tree-like expression"
    # base case: the list is empty.
    if len(tokens) == 0:
        if level == 0:
            return E
        else:
            raise SyntaxError('Unclosed paren.')
    # for the beginning of an expression, add sub-expression to the array
    current_token = tokens.pop(0)
    if current_token == '(':
        # read a new expression and put it into E
        level += 1
        while len(tokens) and tokens[0] != ')':
            E.append(read_from_tokens(tokens,[],level))
            level -= 1
        return E
    # for atom, process it and add it to E, then continue recursive iteration
    elif current_token == ')':
        if level > 0:
            print(E)
            return E
        else:
            raise SyntaxError('Invalid close paren.')
    else:
        A = atom(current_token)
        E.append(A)
        return read_from_tokens(tokens, E, level)

def atom(token: str) -> Atom:
    # first try to convert token to int, failing that float, failing that string
    try:
        return int(token)
    except:
        # this is not ideal!
        try:
            return float(token)
        except:
            return Symbol(token)

result = parse("3 (5 3) 6 (5)")
print(result)