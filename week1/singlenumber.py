def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.v2(nums)
    def v1(self,nums):
        miaou = set()
        for num in nums:
            if num in miaou:
                miaou.discard(num)
            else:
                miaou.add(num)
        return miaou.pop()
    def v2(self,nums):
        miaou = 0
        for num in nums:
            miaou = miaou ^ num
        return miaou
