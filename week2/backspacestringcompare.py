def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        clear_s = []
        clear_t = []
        
        for l in S:
            if l == "#" and clear_s != []:
                clear_s.pop()
            elif l != "#":
                clear_s.append(l)
        
        for l in T:
            if l == "#" and clear_t != []:
                clear_t.pop()
            elif l != "#":
                clear_t.append(l)
        
        return clear_s == clear_t
