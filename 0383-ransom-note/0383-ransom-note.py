class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: b
        """
        freq=[0]*26
        for ch in magazine:
            index=ord(ch)-ord('a')
            freq[index]+=1
        for ch in ransomNote:
            index=ord(ch)-ord('a')
            if freq[index]==0:
                return False
            freq[index]-=1
        return True
        