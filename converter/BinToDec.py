def bintodec(num):
    expo = 1
    decnum = 0
    while (num):
        rem = num % 10
        num = int(num / 10)
        decnum += rem * expo
        expo = expo * 2
    return decnum

