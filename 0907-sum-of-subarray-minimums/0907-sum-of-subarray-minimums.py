class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        pse=[-1]*n
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                pse[i]=stack[-1]
            stack.append(i)

        nse=[n]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                nse[i]=stack[-1]
            stack.append(i)
        total=0
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            total+=arr[i]*left*right
        return total%(10**9+7)
