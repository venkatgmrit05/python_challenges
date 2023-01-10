

def pangrams(s):
    # Write your code here
    total = 2847  # sum of full alphabet with no repetition # lowercase
    lower_s = list(set(s.lower()))
    lower_s = [i for i in lower_s if i.isalpha()]
    lower_s_total = sum(map(ord, lower_s))

    if lower_s_total == total:
        return 'pangram'
    return 'not pangram'


a = 'We promptly judged antique ivory buckles for the next prize'
print(pangrams(a))
