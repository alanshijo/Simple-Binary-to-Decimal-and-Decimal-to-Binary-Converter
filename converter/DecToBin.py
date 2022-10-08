def dectobin(num):
    expo = 1
    bin = 0
    while (num):
        bin += ((num%2) * expo)
        expo = expo * 10
        num = int(num/2)
    return bin