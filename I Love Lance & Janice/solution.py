def strSlice(s):
    str_lst = []

    for i in range(len(s)):
        sliced_str = s[0:i+1]
        str_lst.append(sliced_str)

    return str_lst


def answer(s):

    str_lst = strSlice(s)
    str_len_lst = []

    for elmt in str_lst:
        cnt_elmt = s.count(elmt)
        quotient = len(s)/len(elmt)
        if (elmt * quotient) == s:
            str_len_lst.append(cnt_elmt)

    return max(str_len_lst)