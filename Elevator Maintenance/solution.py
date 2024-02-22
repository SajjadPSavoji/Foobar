def solution(l):
    # sorts semver versions by major/minor/integer
    l.sort(key=lambda val: [int(section) for section in val.split(".")])
    return l