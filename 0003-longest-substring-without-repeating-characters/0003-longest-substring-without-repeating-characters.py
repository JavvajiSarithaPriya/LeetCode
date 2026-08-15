class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        left=0
        n=len(s)
        maxi=0
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            maxi=max(maxi,i-left+1)
        return maxi
        
        