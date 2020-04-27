def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_of_sum = []
        dic_of_seen = {}
        curr_num = 0
        for num in nums:
            list_of_sum.append(curr_num)
            if num == 0:
                curr_num -= 1
            else :
                curr_num +=1
        
        list_of_sum.append(curr_num)
        output = 0
        
        for i,seen in enumerate(list_of_sum):
            if seen not in dic_of_seen:
                dic_of_seen[seen] = i
            else:
                distance = i - dic_of_seen[seen]
                output = max(distance, output)
        return output
