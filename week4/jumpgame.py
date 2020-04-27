def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jump_value = 0
        for i, num in enumerate(nums):
            jump_value = max(jump_value - 1 , num)
            if jump_value == 0 and i != len(nums) - 1:
                return False
            
        return True
                
