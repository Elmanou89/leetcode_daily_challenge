class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._minstack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self._minstack) == 0 or x <= self._minstack[-1]:
            self._minstack.append(x)
        self._stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        elm = self._stack.pop()
        if self._minstack[-1] == elm:
            self._minstack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self._minstack[-1]
        
