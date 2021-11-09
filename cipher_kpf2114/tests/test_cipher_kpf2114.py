from cipher_kpf2114 import cipher_kpf2114
def test_cipher_negshift():
    example = 'weekend'
    expected = 'WEEKEND'
    actual = cipher(example, -26)
    assert actual == expected
