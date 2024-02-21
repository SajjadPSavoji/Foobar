from math import factorial
from collections import Counter
from fractions import gcd

# Burnside's Lemma is used to count the number of distinct orbits 
# (in our case, distinct configurations of the grid) under a group action 
# (here, the group of permutations of rows and columns). It tells us that 
# the number of distinct configurations is the average number of configurations 
# fixed by each permutation.

# Polya Enumeration Theorem extends this by considering not just the permutations
# themselves, but also the colors or states each cell can have. It allows us to
# calculate the generating function for the count of distinct configurations, taking
# into account both the symmetries of the grid and the number of possible states for
# each cell.

def cycle_count(c, n):
    # Calculate the cycle count for a given partition 'c' of 'n'.
    # This function computes the number of distinct permutations that have
    # the cycle structure described by 'c', using the formula for the
    # cycle index of a permutation group.
    cc = factorial(n)
    for a, b in Counter(c).items():
        cc //= (a**b) * factorial(b)
    return cc        

def cycle_partitions(n, i=1):
    # Generate all partitions of 'n', which represent all possible
    # cycle types in the permutations of a set of size 'n'.
    # Each partition corresponds to a unique way of grouping elements
    # into cycles for permutations.
    yield [n]
    for i in range(i, n//2 + 1):
        for p in cycle_partitions(n-i, i):
            yield [i] + p

def solution(w, h, s):
    grid = 0
    # Iterate over all cycle partitions for width 'w' and height 'h'.
    # Each pair of partitions (cpw, cph) represents a unique combination
    # of row and column permutations.
    for cpw in cycle_partitions(w):
        for cph in cycle_partitions(h):            
            m = cycle_count(cpw, w) * cycle_count(cph, h)
            # Calculate the contribution of each pair of partitions to the
            # total count of non-equivalent configurations. This involves
            # raising the number of states 's' to the power of the sum of
            # gcds of all pairs of cycle lengths from 'cpw' and 'cph', which
            # represents the number of invariant configurations under these
            # permutations.
            grid += m * (s**sum([sum([gcd(i, j) for i in cpw]) for j in cph]))
              
    # Divide by factorial(w) * factorial(h) to account for the overcounting
    # from considering all permutations of rows and columns as distinct,
    # when many are equivalent under the group action.
    return str(grid // (factorial(w) * factorial(h)))

# Example usage
print(solution(2, 2, 2))
print(solution(2, 3, 4))