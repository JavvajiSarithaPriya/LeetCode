class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        lent=0
        for ch in s:
            if ch in seen:
                seen.remove(ch)
                lent+=2
            else:
                seen.add(ch)
        if seen:
            lent+=1
        return lent


        