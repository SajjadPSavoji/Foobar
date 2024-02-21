# I will use a mapping function
# that maps char to braille
# it will handle all alphabets
# and space
# solution has O(n) time
# and O(n) space
def solution(s):
    # braille string
    b = ""
    # mapping dict
    braille_alphabet = {
        'a': '100000',
        'b': '110000',
        'c': '100100',
        'd': '100110',
        'e': '100010',
        'f': '110100',
        'g': '110110',
        'h': '110010',
        'i': '010100',
        'j': '010110',
        'k': '101000',
        'l': '111000',
        'm': '101100',
        'n': '101110',
        'o': '101010',
        'p': '111100',
        'q': '111110',
        'r': '111010',
        's': '011100',
        't': '011110',
        'u': '101001',
        'v': '111001',
        'w': '010111',
        'x': '101101',
        'y': '101111',
        'z': '101011',
        ' ': '000000',
        'CAPITAL': '000001'
    }
    # loop over chars of s
    # and convert one by one
    for c in s:
      if c.isupper():
        b += braille_alphabet['CAPITAL']
      b+= braille_alphabet[c.lower()]

    return b