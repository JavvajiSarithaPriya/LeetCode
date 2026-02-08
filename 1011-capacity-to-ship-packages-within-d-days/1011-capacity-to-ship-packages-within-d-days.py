class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            req_days=1
            current_load=0
            for w in weights:
                if current_load+w<=mid:
                    current_load+=w
                else:
                    req_days+=1
                    current_load=w
            if req_days<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        