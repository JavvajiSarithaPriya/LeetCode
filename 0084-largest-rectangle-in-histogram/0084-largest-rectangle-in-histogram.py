class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        ln=[-1]*n
        rn=[n]*n
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                ln[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                rn[i]=stack[-1]
            stack.append(i)
        ans=0
        for i in range(n):
            width=rn[i]-ln[i]-1
            area=heights[i]*width
            ans=max(ans,area)
        return ans

        