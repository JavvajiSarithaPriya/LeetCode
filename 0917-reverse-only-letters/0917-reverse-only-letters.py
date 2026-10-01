class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        li=[]
        for ch in s:
            if ch.isalpha():
                li.append(ch)
        j=len(li)-1
        res=[]
        for ch in s:
            if ch.isalpha():
                res.append(li[j])
                j-=1
            else:
                res.append(ch)
        return ''.join(res)
        