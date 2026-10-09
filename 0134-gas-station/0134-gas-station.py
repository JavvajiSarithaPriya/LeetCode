class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gases=0
        costs=0
        tank=0
        start=0
        for i in range(len(cost)):
            gases+=gas[i]
            costs+=cost[i]
            tank+=gas[i]-cost[i]
            if tank<0:
                start=i+1
                tank=0
        if gases<costs:
            return -1
        return start


        