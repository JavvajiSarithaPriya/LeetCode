class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        
        for row in range(numRows):
            cur=1
            temp=[1]
            for col in range(row):
                cur=cur*(row-col)
                cur=cur//(col+1)
                temp.append(cur)
            ans.append(temp)
        return ans