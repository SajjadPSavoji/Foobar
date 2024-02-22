def solution(L):
  def remove(L, n, m):
    # remove n elements from top where n%3=m
    output = []
    for l in L:
      if n > 0 and l%3==m:
        n -= 1
        continue
      output.append(l)
    return output

  def get_stats(L):
    # get frequencies and mod of sum
    freq = [0, 0, 0]
    all_mod = 0
    for l in L:
      freq[l%3] += 1
      all_mod = (all_mod + l)%3
    return freq, all_mod

  if len(L) == 0:
    return 0
  L.sort()
  freq, all_mod = get_stats(L)

  # based on all_mod
  # either remove two 1s / one 2s
  # or remove one 2s / two 1s
  if all_mod == 0:
    output = L
  elif all_mod == 1:
    if freq[1] >= 1:
      output = remove(L, 1, 1)
    elif freq[2] >= 2:
      output = remove(L, 2, 2)
    else:
      return 0
  elif all_mod == 2:
    if freq[2] >= 1:
      output = remove(L, 1, 2)
    elif freq[1] >= 2:
      output = remove(L, 2, 1)
    else:
      return 0

  if len(output) ==0:
    return 0

  return int("".join(map(str, output[::-1])))