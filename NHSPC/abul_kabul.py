i, j = list(map(int, input().split()))
odd = i - (i // 2)
print(odd * 2 + (j - odd) * 1 if odd <= j else j * 2)