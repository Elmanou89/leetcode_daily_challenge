def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        begin = 0
        end = len(nums) - 1
        mid = (begin + end) // 2
        while begin <=  end:
            if nums[mid] == target:
                return mid
            
            if  nums[begin] <= nums[mid] :
                if nums[begin] <= target <= nums[mid]:
                    end = mid
                else :
                    begin = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    begin = mid + 1
                else:
                    end = mid
            
            mid = (begin + end) // 2
        return -1
