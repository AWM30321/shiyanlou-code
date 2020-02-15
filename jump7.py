for a in range(1,101):
    if a % 7 ==0:
        continue
    else:
        string = str(a)
        if string.endswith('7'):
            continue
    print(a)
