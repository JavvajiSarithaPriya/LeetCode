class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m*k>len(bloomDay):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            boq=0
            flow=0
            for day in bloomDay:
                if day<=mid:
                    flow+=1
                    if flow==k:
                        boq+=1
                        flow=0
                else:
                    flow=0
            if boq>=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        