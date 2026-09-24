class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        e=0
        o=0
        for i in range(len(num)):
            if i%2==0:
                e+=int(num[i])
            else:
                o+=int(num[i])
        return e==o
        