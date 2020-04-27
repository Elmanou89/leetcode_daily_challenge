def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pter_non_0 = 0
        for i,num in enumerate(nums):
            if num != 0:
                nums[i] = nums[pter_non_0]
                pter_non_0 += 1
        
