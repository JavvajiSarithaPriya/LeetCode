class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        chars=sorted(freq,key=freq.get,reverse=True)
        result=""
        for ch in chars:
            result+=ch*freq[ch]
        return result
