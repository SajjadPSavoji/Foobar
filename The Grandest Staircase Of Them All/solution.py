from math import ceil as ceil_float
from math import sqrt as sqrt
ceil = lambda x: int(ceil_float(x))

#################################################
# A Dynamic programming approach
#  -> o(n^2) time
#  -> o(n^2) space
##################################################
# Problem is rephrased as number of possible steps
# with at least 1 step (instaed of 2 steps)
# and max hight of "h"
# and number of bricks "m"
# then the solution will be f(n, n) -1
# removing the case of one step with n bricks
##################################################
# for each step of DP, take k bricks for first step
# reduce m by k [k brkcks taken from m bricks]
# set h to k-1 [max h of sub stair should be k-1]
# for m bricks min hight of stair is computed by
# h_min = ceil(sqrt(2*m + 1./4) - 1./2)
# by solving 1 + 2 + ... + h_min = m
###################################################
# f(m, h) = \sum_{k=h_min}^{min(m, h)}{f(m-k, k-1)}
###################################################

def solution(n):
    # (m, h) -> number of combinations
    cache = {}

    # init boundry conditions
    for m in xrange(n+1):
        cache[(m, 0)] = 0
    for h in xrange(n+1):
        cache[(0, h)] = 1
        # this will overwrite (0, 0) -> 1

    # fill in table/cache
    for m in xrange(1, n+1):
        h_min = ceil(sqrt(2*m + 1./4) - 1./2)
        for h in xrange(1, n+1):
            v_mh = 0
            if h >= h_min:
                for k in xrange(h_min, min(h, m)+1):
                    v_mh += cache[(m-k, k-1)]
            cache[(m, h)] = v_mh

    # anser is (m=n, h=n) -1 (at least two steps)
    return cache[(n, n)] - 1