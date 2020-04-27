def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    def toHappy(number):
        somme = 0
        while number > 0 :
            somme += (number % 10) * (number % 10)
            number = number // 10
        return somme
    gogo=n
    miaou = {}
    while gogo != 1 :
        if gogo in miaou:
            return False
        miaou[gogo] = 1
        gogo = toHappy(gogo)
    return True
