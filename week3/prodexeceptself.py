def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]*len(nums)
        curr_prod = 1
        for i in range(len(nums)):
            output[i] = output[i] * curr_prod
            curr_prod = curr_prod * nums[i]
        curr_prod = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i] * curr_prod
            curr_prod = curr_prod * nums[i]
        
        return output
