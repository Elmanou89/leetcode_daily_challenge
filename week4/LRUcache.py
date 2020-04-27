#not proud of this one 
import heapq
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._max_cap = capacity
        self._container = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for i,val in enumerate(self._container):
            if val[0] == key:
                tmp = self._container.pop(i)
                self._container = [tmp] + self._container
                return val[1]
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        found = False
        for i,val in enumerate(self._container):
            if key==val[0]:
                self._container.pop(i)
                self._container = [(key,value)] + self._container
                found = True
        if not found: 
            if len(self._container) == self._max_cap:
                self._container.pop()
            self._container = [(key,value)] + self._container
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
