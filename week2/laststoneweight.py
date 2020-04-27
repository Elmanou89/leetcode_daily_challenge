def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-x for x in stones]
        heapify(stones)
        while len(stones) > 1:
            stone1 = heappop(stones)
            stone2 = heappop(stones)
            if stone1 != stone2:
                heappush(stones,-abs(stone1 - stone2) )
        if len(stones) == 0:
            return 0
        return -stones[0]
