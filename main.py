print("задание 19:")


def f(x, y, h):
    if h == 2:
        return f(max(x, y) * 2, min(x, y), h + 1)
    if x + y > 99 and h == 3:
        return True
    elif x + y <= 99 and h == 3:
        return False
    elif x + y > 99:
        return False
    return f(x + 3, y, h + 1) and f(x, y + 3, h + 1) and f(x * 2, y, h + 1) and f(x, y * 2, h + 1)


for i in range(1, 89):
    if f(10, i, 1) is True:
        print(i)
        break


print("задание 20:")


def f(x, y, h):
    if x + y > 99 and h == 4:
        return True
    elif x + y <= 99 and h == 4:
        return False
    elif x + y > 99:
        return False
    if h % 2 == 0:
        return f(x + 3, y, h + 1) and f(x, y + 3, h + 1) and f(x * 2, y, h + 1) and f(x, y * 2, h + 1)
    else:
        return f(x + 3, y, h + 1) or f(x, y + 3, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)


for i in range(1, 89):
    if f(10, i, 1) is True:
        print(i)


print("задание 21:")


def f(x, y, h):
    if x + y > 99 and (h == 3 or h == 5):
        return True
    elif x + y <= 99 and h == 5:
        return False
    elif x + y > 99:
        return False
    if h % 2 == 1:
        return f(x + 3, y, h + 1) and f(x, y + 3, h + 1) and f(x * 2, y, h + 1) and f(x, y * 2, h + 1)
    else:
        return f(x + 3, y, h + 1) or f(x, y + 3, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)


def f_pr(x, y, h):
    if x + y > 99 and (h == 3):
        return True
    elif x + y < 100 and h == 5:
        return False
    elif x + y > 99:
        return False
    if h % 2 == 1:
        return f_pr(x + 3, y, h + 1) and f_pr(x, y + 3, h + 1) and f_pr(x * 2, y, h + 1) and f_pr(x, y * 2, h + 1)
    else:
        return f_pr(x + 3, y, h + 1) or f_pr(x, y + 3, h + 1) or f_pr(x * 2, y, h + 1) or f_pr(x, y * 2, h + 1)


print("либо 1, либо 2:")
for i in range(1, 89):
    if f(10, i, 1) is True:
        print(i)
print("только 1:")
for i in range(1, 89):
    if f_pr(10, i, 1) is True:
        print(i)