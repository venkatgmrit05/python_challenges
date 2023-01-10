import os

"""
func : x1*x2*x3*x4  + x1^2 * X3^2   + x1*x3*x4 + 3*x2^3 + 8
>>         term1    + term2         + term3    + term4  + constant

[
    (k,v),                      #constant
    ((c,v),[(x,v,p),(x,v,p),..])_1, #term1 
    ((c,v),[(x,v,p),(x,v,p),..])_2, #term2
    ((c,v),[(x,v,p),(x,v,p),..])_3, #term3 
    .
    .
    ((c,v),[(x,v,p),(x,v,p),..])_N, #termN

]
"""
# function builder


def build_function(terms):
    k, *rest_terms = terms  # first item is always constant

    func_str, func = k
    func_strs = [func_str, ]
    func_num_strs = [f"{func}", ]
    for rt_ in rest_terms:
        func_num_str, func_str_, func_ = build_term(rt_)
        func_strs.append(func_str_)
        func_num_strs.append(func_num_str)

        func += func_

    func_str = ' + '.join(func_strs)
    func_num_str = ' + '.join(func_num_strs)

    return func_num_str, func_str, func

# term builder


def build_term(items: list):
    c, *ritems = items  # first item is always coeff
    term_str, term_ = c

    term_strs = [term_str, ]
    term_num_strs = [f"{term_}", ]
    for rit in ritems[0]:
        ri, v, p = rit
        term_strs.append(f"{ri}^{p}")
        term_num_strs.append(f"{v}^{p}")
        term_ *= v**p

    term_str = '*'.join(term_strs)
    term_num_strs = '*'.join(term_num_strs)

    return term_num_strs, term_str, term_


if __name__ == "__main__":

    terms = [
        8,
        (1, [('x1', 1), ('x2', 1), ('x3', 1), ('x4', 1)]),
        (1, [('x1', 2), ('x3', 2)]),
        (1, [('x1', 1), ('x3', 1), ('x4', 1)]),
        (3, [('x2', 3), ]),
    ]

    terms = [
        # ('var_name', val), #('var_name',val,power)
        ('k', 0),
        (('c1', 1), [('x1', 10.5, -2), ('y1', 10, 3), ]),
        (('c2', 1), [('x2', 5, -1), ('z1', 5, -2)]),
    ]

    # quaratic equation
    terms = [
        # ('var_name', val), #('var_name',val,power)
        ('k', 0),
        (('c1', 1), [('x1', 10, 2), ]),
        (('c2', 1), [('x2', 5, 2), ]),
    ]

    f_num_str, f_str, f = build_function(terms)
    print(f"f = {f_str}\n")
    print(f"{f_str} = {f}\n")
    print(f"{f_num_str} = {f}\n")

    # cubic equation
    terms = [
        # ('var_name', val), #('var_name',val,power)
        ('k', 0),
        (('c1', 1), [('x1', 10, 3), ]),
        (('c2', 1), [('x2', 5, 3), ]),
    ]

    f_num_str, f_str, f = build_function(terms)
    print(f"f = {f_str}\n")
    print(f"{f_str} = {f}\n")
    print(f"{f_num_str} = {f}\n")
