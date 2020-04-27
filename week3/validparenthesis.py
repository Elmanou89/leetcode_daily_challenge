def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = 0
        closing = 0
        for c in  s:
            if c == ')':
                closing +=1
            else:
                opening += 1
            if closing > opening:
                return False
        opening = 0
        closing = 0
        for c in s[::-1]:
            if c == '(':
                closing +=1
            else:
                opening += 1
            if closing > opening:
                return False
        return True
