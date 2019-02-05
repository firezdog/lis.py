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

def read_from_tokens(tokens: list, E=[]) -> Exp:
    "convert a string into a tree-like expression"
    # base case: the list is empty.
    if len(tokens) == 0:
        return E
    # for the beginning of an expression, add sub-expression to the array
    now = tokens.pop(0)
    if now == '(':
        # read a new expression and put it into E
        while len(tokens) and tokens[0] != ')':
            E.append(read_from_tokens(tokens,[]))
        return E
    # for atom, process it and add it to E, then continue recursive iteration
    elif now == ')':
        return E
    else:
        A = atom(now)
        E.append(A)
        return read_from_tokens(tokens, E)

def atom(token: str) -> Atom:
    # first try to convert token to int, failing that float, failing that string
    try:
        return int(token)
    except:
        # this is not ideal
        try:
            return float(token)
        except:
            return token

result = parse("3 4 )")
print(result)