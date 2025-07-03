from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for value in nums:
            if abs(value) < abs(closest):
                closest = value
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
        
numbers = [22,-11,11,5,6,10,-10,1,0]
problem = Solution()

print("The solution is: " + str(problem.findClosestNumber(numbers)))