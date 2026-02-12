class Solution:
    def kthElement(self, a, b, k):
        # code here
        arr=a+b
        l=sorted(arr)
        return l[k-1]
        