class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''n=len(height)
        lm=[0]*n
        rm=[0]*n
        lm[0]=height[0]
        for i in range(1,n):
            lm[i]=max(lm[i-1],height[i])
        rm[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rm[i]=max(rm[i+1],height[i])
        total=0
        for i in range(n):
            total+=max((min(lm[i],rm[i]))-height[i],0)
        return total'''
        left=0
        right=len(height)-1
        leftmax=0
        rightmax=0
        water=0
        while left<=right:
            if height[left]<=height[right]:
                if height[left]>=leftmax:
                    leftmax=height[left]
                else:
                    water+=leftmax-height[left]
                left+=1
            else:
                if height[right]>=rightmax:
                    rightmax=height[right]
                else:
                    water+=rightmax-height[right]
                right-=1
        return water