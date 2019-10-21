def lucas(x):
    if x < 1:
        return 0
    if x == 1:
        return 2
    if x == 2:
        return 1
    return lucas(x - 1) + lucas(x - 2)