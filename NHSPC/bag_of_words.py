for _ in range(int(input())):
    input_ = input()
    inp = (int(input_[0:2]) - 9) * 60 + int(input_[2:])
    print(inp // 5 * 8 - inp // 15 * 8)