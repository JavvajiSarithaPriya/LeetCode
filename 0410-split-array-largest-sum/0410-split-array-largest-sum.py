class Solution:
    def splitArray(self, nums, m):
        # Search space
        low = max(nums)        # minimum possible answer
        high = sum(nums)       # maximum possible answer
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if self.canSplit(nums, m, mid):
                ans = mid          # possible, try smaller
                high = mid - 1
            else:
                low = mid + 1      # not possible, increase

        return ans

    def canSplit(self, nums, m, maxSum):
        count = 1          # number of subarrays
        current_sum = 0

        for num in nums:
            if current_sum + num <= maxSum:
                current_sum += num
            else:
                count += 1
                current_sum = num

                if count > m:      # need more than m parts → fail
                    return False

        return True
