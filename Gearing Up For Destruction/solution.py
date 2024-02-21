def solution(pegs):
  # check list not empty
  if len(pegs) == 0:
    return [-1, -1]

  # check list sorted
  pegs = sorted(pegs)
  n = len(pegs)-1
  sum = 0
  muli = -1
  for i in range(1, n+1):
    li = pegs[i] - pegs[i-1]
    muli *= -1
    sum += muli * li

  # check all rs >=1
  r0 = (2 * sum)/(2 + muli)
  r_prev = r0
  for i in range(1, n+1):
    li = pegs[i] - pegs[i-1]
    ri = li - r_prev
    r_prev = ri
    if ri < 1:
      return [-1, -1]

  # check if r0 >= 1
  if r0 >= 1:
    # convert to simple form
    if (2 * sum)%(2 + muli) == 0:
      return [int((2 * sum)/(2 + muli)), 1]
    else:
      return [int(2 * sum), int(2 + muli)]
  else:
    return [-1, -1]