def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = {}
        for i in range(len(text1)):
            for j in range(len(text2)):
                is_same_char = 1 if text1[i] == text2[j] else 0
                if j > 0 and i > 0:
                    if is_same_char == 1:
                        dp[(i,j)] = dp[(i-1,j-1)] + 1 
                    else:
                        dp[(i,j)] = max(dp[(i,j-1)],dp[(i-1,j)] ) 
                elif i > 0:
                    dp[(i,j)]  = max(dp[(i-1,j)], is_same_char)
                elif j > 0:
                    dp[(i,j)]  = max(dp[(i,j-1)]  , is_same_char)
                else:
                    dp[(i,j)]  = is_same_char
        return dp[(len(text1)-1,len(text2)-1)]
