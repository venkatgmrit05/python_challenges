"""
Implement the function embolden(s, lst) which takes in a
string s and list of substrings lst, and wraps all substrings
    in s with an HTML bold tag <b> and </b>.
If two bold tags overlap or are contiguous, they should be merged.

For example, given s = abcdefg and lst = ["bc", "ef"], return the string a<b>bc</b>d<b>ef</b>g.

Given s = abcdefg and lst = ["bcd", "def"], return the string a<b>bcdef</b>g, since they overlap.
"""


# def embolden(s, lst):


#     ret = "a<b>bcdef</b>g"
#     ret = None
#     return ret

def combine_str(a, b, on_common=True):

    aletters = [i for i in a]
    bletters = [i for i in b]

    longw = a
    shortw = b
    long_lst = aletters
    short_lst = bletters

    common = [i for i in short_lst if i in long_lst]

    if common:
        common_substr = ''.join(common)
        combined_str = ''.join(longw).replace(common_substr, shortw)
    else:
        common_substr = None
        if on_common:  # combine only if common substr exists

            combined_str = None
        else:
            combined_str = a+b
    return combined_str, common_substr


def combine_list(lst: list, unqiue_str=[]):

    num_items = len(lst)
    print('\n')
    print(lst)
    i = 0
    while i < num_items-1:
        print(f'combining item {i}')
        firstw = lst.pop(i)
        print(firstw)
        count = 0
        for nextw in lst:
            print('\t', nextw)
            count = +1
            if count < 100:
                ret, common_substr = combine_str(firstw, nextw)

                if common_substr is not None:
                    print('\t\t', ret, common_substr)
                    lst.remove(nextw)
                    lst.insert(0, ret)
                    nlst = lst.copy()
                    print('\t\t\t', nlst)
                    unqiue_str.append(nextw)
                    unqiue_str.append(ret)
                    return combine_list(nlst, unqiue_str)

        # unqiue_str.append(firstw)
        i += 1

    print("final:", lst)
    print("unique:", unqiue_str)

    # else:
    #     unqiue_str.append


def combine_list0(lst: list, unqiue_str=[]):
    nlst = []
    for i in range(len(lst)-1):
        print(lst)
        a, b = lst[i], lst[i+1]
        if len(a) < len(b):
            a, b = b, a

        if a[:-len(b)] == b[:len(b)]:
            nlst.append(combine_str(a, b)[0])
            # return combine_list(nlst, unqiue_str)
            print(nlst)
        else:
            nlst.append(a)
            print(nlst)
    print(nlst)


if __name__ == "__main__":  # pragma: no cover
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
        }
    }

    def run_test(fnc: object, test_params: dict):
        for _test in test_params:
            out = fnc(test_params[_test]['inputs']['s'],
                      test_params[_test]['inputs']['lst'])
            assert out == test_params[_test][
                'output'], f"output doesnt match. actual  is {out} \n required is {test_params[_test]['output']}"

    # run_test(embolden, test_params)

    lst = ["ab", "c", "cd", "de"]

    combine_list(lst)

    # lst = ["ab", "bc", "cd", "de"]
    # print('\n')
    # print(lst)
    # firstw = lst.pop(0)
    # print(firstw)
    # count = 0
    # for nextw in lst:
    #     print('\t', nextw)
    #     count = +1
    #     if count < 100:
    #         ret, common_substr = combine_str(firstw, nextw)

    #         if common_substr is not None:
    #             print('\t\t', ret, common_substr)
    #             lst.remove(nextw)
    #             lst.insert(0,ret)
    #             nlst = lst.copy()
    #             print('\t\t\t', nlst)

    #     if common_substr is None:
    #         lst.insert(0, ret)
    #         print(lst)
    #     else:
    #         lst.insert(0, ret)
    #         print(lst)
    # else:
    #     break
