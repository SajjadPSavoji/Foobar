# o(n)
def solution(start, length):
  def xor_0b(b):
    # compute xor of range [0, b]
    if b < 0:
      return 0
    m4_b = b%4
    if m4_b == 0:
      return b
    elif m4_b == 1:
      return 1
    elif m4_b == 2:
      return b + 1
    else: # m4_b == 3
      return 0

  def xor_ab(a, b):
    # computes xor or range[a, b]
    # assume a >= 0
    # assuming b >= a
    return xor_0b(a-1) ^ xor_0b(b)

  check_sum = 0
  for i in range(length):
      a_i = start + i*length
      b_i = start + i*length + length-i-1
      check_sum ^= xor_ab(a_i, b_i)
  return check_sum