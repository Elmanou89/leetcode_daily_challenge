def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic_of_answers = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))        
            if sorted_word in dic_of_answers:
                dic_of_answers[sorted_word].append(word)
            else:
                dic_of_answers[sorted_word] = [word]
        
        output = []
        for answer in dic_of_answers:
            output.append(dic_of_answers[answer])
            
        return output
