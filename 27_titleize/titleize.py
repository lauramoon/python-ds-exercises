def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # didn't know there was already a method for this...
    
    lst = phrase.split(' ')
    cap_lst = [word.capitalize() for word in lst]
    return ' '.join(cap_lst)