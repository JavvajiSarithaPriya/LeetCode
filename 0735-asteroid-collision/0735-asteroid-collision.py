class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for asa in asteroids:
            while stack and stack[-1]>0 and asa<0:

                if stack[-1]<abs(asa):
                    stack.pop()
                    continue
                elif stack[-1]==abs(asa):
                    stack.pop()
                    asa=0
                    break
                else:
                    asa=0
                    break
            if asa!=0:
                stack.append(asa)
        return stack

        