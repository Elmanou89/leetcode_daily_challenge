def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        total_shift = 0
        for sh in shift:
            direction = sh[0]
            amount = sh[1] if direction != 0 else -sh[1]
            total_shift += amount
        
        output = s
        if total_shift > 0:
            for i in range(total_shift):
                output = output[-1] + output[:-1]
        elif total_shift < 0 :
            for i in range(-total_shift):
                output = output[1:] + output[0]
        
        return output
