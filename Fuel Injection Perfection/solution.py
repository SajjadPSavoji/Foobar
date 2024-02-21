# the impact of +1 and -1
# will stay confined to the
# first two digits of binary rep
# xxx(01) -> subtract -> xxx(00)
# xxx(11) -> addition -> xxx(00)
def solution(n):
    # convert to long
    # long has no digit limits
    n = long(n)
    count = 0
    while n != 1:
        if n % 2:
            if n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        else:
            n /= 2
        count += 1
    return count

print(solution(4))
print(solution(15))