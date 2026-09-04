class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[-1]*len(nums)
        stack=[]
        n=len(nums)
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1]<=nums[i%n]:
                stack.pop()
            if i<n:
                if stack:
                    ans[i]=stack[-1]
            stack.append(nums[i%n])
        return ans
        
