def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # made this too complicated - I misread the last test as testing '(")()(")'
    # and thought it should be false because of the placement of the quote marks
    # but now I see we're only testing the parens inside the quote marks
    # (and I don't know why my first (unsaved) version failed)

    total = 0
    in_quote_total = 0
    in_quote = False
    for char in parens:
        if char in ['(', ')']:
            step = 1 if char == '(' else -1
            total = total + step
            if in_quote:
                in_quote_total = in_quote_total + step
        if char == '"':
            in_quote = not in_quote
        if total < 0 or in_quote_total < 0:
            return False
    if total != 0 or in_quote_total !=0:
        return False
    return True

        

