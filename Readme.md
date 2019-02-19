# About the Lisp API *(courtesy of Wikipedia)

Every expression is enclosed in parentheses.\
An expression consists of an operation followed by its arguments.\
Arguments may themselves be expressions.\

## Conses and Lists
Originally (but not in lis.py) lisp's lists were implemented as singly linked lists. A node was called a "cons" and contained two pointers, "car" (to data) and "cdr" (to the next).

"If a given cons is taken to be the head of a linked list, then its car points to the first element of the list, and its cdr points to the rest of the list."  Or, so it would seem, the data contained in a given node should be the result of applying its "car" to its "cdr" -- of evaluating its "cdr" with the operation specified in "car". (?)

e.g. (+ (1 3)) -- the arguments in the list (1 3) are evaluated with "+" (though in this implementation and some others I have seen, the remaining arguments do not need to be enclosed in parentheses -- nor is the data stored in the form e.g. ['+', [1, 3]].  But if a list were to be composed of a series of nodes with only two pointers, this would seem to be the necessary form of an expression.