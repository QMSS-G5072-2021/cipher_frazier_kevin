def cipher(text, shift, encrypt=True):
    """
    Encrypts strings by shifting each letter a specified number of places right or left in the alphabet. Can also decrypt strings the same way.

    Parameters
    ----------
    text : str
      The text you will encrypt/decrypt
    shift : int
      The amount you want to shift right or left in alphabet.
     encrypt: bool (default=True)
      A boolean that defines whether you are encrypting or decrypting the text

    Returns
    -------
    str
      The encrypted or decrypted result

    Examples
    --------
    >>> from cipher_kpf2114 import cipher_kpf2114
    >>> text = 'hello'
    >>> shift = 10
    >>> cipher(text, shift, encrypt=True)
    'rovvy'
    >>> from cipher_kpf2114 import cipher_kpf2114
    >>> text = 'iwpCzHvxKxCv'
    >>> shift = 15
    >>> cipher(text, shift, encrypt=False)
    'Thanksgiving'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
