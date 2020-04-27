def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        L = len(nums)
        output = 0
        
        cum_sum = {i:sum(nums[:i]) for i in range(L+1)}
        dict_of_sum = {}
        for i in range(L+1):
            if (cum_sum[i] - k) in dict_of_sum:
                output += dict_of_sum[(cum_sum[i] - k)]
                
            if cum_sum[i] in dict_of_sum:
                dict_of_sum[cum_sum[i]] += 1
            else:
                dict_of_sum[cum_sum[i]] = 1

        return output
