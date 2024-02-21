# will try an O(n) solution
# will only count the number of
# people from one side of helo
# and multiply by two
def solution(s):
    right = '>'
    left  = '<'
    tot_rights_so_far = 0
    tot_salutes = 0
    # iterate from left to right
    # and count numbers of total
    # right-going employee
    # at each left going employee
    # add up the nmber of solutes by two
    for c in s:
      if c == right:
        tot_rights_so_far += 1
      elif c == left:
        tot_salutes += tot_rights_so_far
      else:
        continue

    return tot_salutes * 2