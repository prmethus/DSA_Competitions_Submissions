wt = {
    '0': 'abcdef',
    '1': 'bc',
    '2': 'abdeg',
    '3': 'abcdg',
    '4': 'bcfg',
    '5': 'acdfg',
    '6': 'acdefg',
    '7': 'abc',
    '8': 'abcdef',
    '9': 'abcdfg'
}

t = input()
print(''.join(wt[i] for i in list(t)))