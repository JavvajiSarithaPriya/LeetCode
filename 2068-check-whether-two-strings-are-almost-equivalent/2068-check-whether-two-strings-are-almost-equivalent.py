
class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        for ch in "abcdefghijklmnopqrstuvwxyz":
            count1 = word1.count(ch)
            count2 = word2.count(ch)

            if abs(count1 - count2) > 3:
                return False

        return True
