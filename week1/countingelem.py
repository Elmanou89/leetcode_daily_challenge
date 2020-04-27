def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dic = {}
        
        for elm in arr:
            dic[elm] = 1
            
        count = 0
        for elm in arr:
            if elm + 1 in arr:
                count += 1
        return count
