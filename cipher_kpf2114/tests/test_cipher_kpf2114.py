from cipher_kpf2114 import cipher_kpf2114
import pytest
def cipher(text, shift, encrypt=True):
    assert isinstance(shift, str) == False, "Cannot use strings for shift values"
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

def test_cipher_negshift():
    example = 'weekend'
    expected = 'WEEKEND'
    actual = cipher(example, -26)
    assert actual == expected
