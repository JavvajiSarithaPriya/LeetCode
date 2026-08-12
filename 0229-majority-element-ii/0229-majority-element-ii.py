class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        freq={}
        li=[]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in freq:
            if freq[num]>n//3:
                li.append(num)
        return li
        