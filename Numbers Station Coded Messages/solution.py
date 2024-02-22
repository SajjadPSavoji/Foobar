def solution(l, t):
    # return first beginning and end indexes in l whose values add up to t
    for start in range(len(l)):
        total = 0
        for current, e in enumerate(l[start:]):
            total += e
            if total == t:
                return [start, start + current]
            if total > t:
                break
    return [-1, -1]