def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # Either of these would be less efficient that the provided solution
    # with one iteration through the phrase

    return {char: phrase.lower().count(char) for char in phrase.lower() if char in 'aeiou'}
    # This also works, but second test dictionary ordered differently than in doc test:
    # return {vowel: phrase.lower().count(vowel) for vowel in 'aeiou' if vowel in phrase.lower() }