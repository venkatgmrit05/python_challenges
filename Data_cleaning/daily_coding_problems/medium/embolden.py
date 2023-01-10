"""
Implement the function embolden(s, lst) which takes in a
string s and list of substrings lst, and wraps all substrings
    in s with an HTML bold tag <b> and </b>.
If two bold tags overlap or are contiguous, they should be merged.

For example, given s = abcdefg and lst = ["bc", "ef"], return the string a<b>bc</b>d<b>ef</b>g.

Given s = abcdefg and lst = ["bcd", "def"], return the string a<b>bcdef</b>g, since they overlap.
"""


def in_sequence(a, b):
    in_sequence = None
    if len(b) > len(a):
        a, b = b, a

    len_b = len(b)
    # if a[-len_b:] == b:
    if a[-len_b] == b[0]:
        in_sequence = True
    else:
        in_sequence = False
    return in_sequence


def combine_str(a, b, on_common=True):

    aletters = [i for i in a]
    bletters = [i for i in b]

    longw = a
    shortw = b
    long_lst = aletters
    short_lst = bletters

    common = [i for i in short_lst if i in long_lst]
    common_substr = ''.join(common)
    if common_substr:

        abin_sequence = in_sequence(a, common_substr)
        if abin_sequence:
            combined_str = ''.join(longw).replace(common_substr, shortw)
        else:
            combined_str = None
    else:
        if on_common:  # combine only if common substr exists
            combined_str = None
        else:
            combined_str = a+b
    return combined_str, common_substr


def combine_list(lst: list):
    comb = []

    while len(lst) != 0:
        ret = lst.pop(0)
        for nitem in lst:
            cret, _ = combine_str(ret, nitem)
            if cret is not None:
                ret = cret
                lst.remove(nitem)
                lst.insert(0, ret)
        if ret not in comb:
            comb.append(ret)

    return comb


def embolden(s, lst):

    delim1 = '<b>'
    delim2 = '</b>'

    substr = []
    lst = combine_list(lst)
    for i in lst:
        toks = s.split(i)
        istr = f"{delim1}{i}{delim2}"
        substr.append(istr)
        ns = istr.join(toks)
        s = ns
        print(s)
    return s


if __name__ == "__main__":  # pragma: no cover

    # # dev
    # lst = ["ab", "c", "cd", "de"]
    # lst = ["a", "c", "cd", "bde"]
    lst = ["bc", "def", "fc"]
    print(combine_list(lst))

    # s = "abcdeffc"
    # lst = ["bc", "def", "fc"]
    # embolden(s, lst)

    # test
    test_params = {
        1: {
            "inputs": {
                "s": "abcdefg",
                "lst": ["bc", "ef"],
            },
            "output": "a<b>bc</b>d<b>ef</b>g"
        },
        2: {
            "inputs": {
                "s": "abcdefg",
                "lst": ["bcd", "def"],
            },
            "output": "a<b>bcdef</b>g"
        },
        3: {
            "inputs": {
                "s": "abcdeffc",
                "lst": ["bc", "def", "fc"],
            },
            "output": "a<b>bc</b><b>def</b><b>fc</b>"
        }
    }

    def run_test(fnc: object, test_params: dict):
        for _test in test_params:
            out = fnc(test_params[_test]['inputs']['s'],
                      test_params[_test]['inputs']['lst'])
            assert out == test_params[_test][
                'output'], f"output doesnt match. actual  is {out} \n required is {test_params[_test]['output']}"

    #run_test(embolden, test_params)
