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

        

