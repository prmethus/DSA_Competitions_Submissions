num = int(input())
ot = 1
for i in range(1, num // 2 + 1):
    if int(num / i) == num / i:
        ot += 1
print(ot)
if ot > 2:
    print("Never give up")
else:
    print("Well done")