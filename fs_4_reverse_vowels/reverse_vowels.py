def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    lst = list(s)
    v_lst = [char for char in lst if char.lower() in 'aeiou']
    v_lst.reverse()
    v_pos = [i for i in range(len(s)) if s[i].lower() in 'aeiou']
    for i in range(len(v_pos)):
        lst[v_pos[i]] = v_lst[i]
    return ''.join(lst)
