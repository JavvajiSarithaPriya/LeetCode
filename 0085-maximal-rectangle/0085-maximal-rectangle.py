class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        row=len(matrix)
        col=len(matrix[0])
        hi=[0]*col
        maxarea=0
        for r in range(row):
            for c in range(col):
                if matrix[r][c]=='1' or matrix[r][c]==1:
                    hi[c]+=1
                else:
                    hi[c]=0
            ln=[-1]*col
            rn=[col]*col
            stack=[]
            for i in range(col):
                while stack and hi[stack[-1]]>=hi[i]:
                    stack.pop()
                if stack:
                    ln[i]=stack[-1]
                stack.append(i)


            stack=[]
            for i in range(col-1,-1,-1):
                while stack and hi[stack[-1]]>=hi[i]:
                    stack.pop()
                if stack:
                    rn[i]=stack[-1]
                stack.append(i)
            for i in range(col):
                width=rn[i]-ln[i]-1
                area=hi[i]*width
                maxarea=max(maxarea,area)
        return maxarea

        