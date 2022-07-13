def even_or_odd():
        _ = input()
        li = list(map(int, input().split()))
        print(*[0 if i % 2 == 0 else 1 for i in li ])

even_or_odd()