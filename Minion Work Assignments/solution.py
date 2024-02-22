def solution(data, n):
    ret = []
    for e in data:
        if data.count(e) <= n:
            ret.append(e)
    return ret