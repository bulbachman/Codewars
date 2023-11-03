class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {} # val : index

        for i,n in enumerate(nums):
            print(i,n)
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
            print(prevMap)
        return


solutionobject = Solution()
print(solutionobject.twoSum([3, 3], 6))
print(solutionobject.twoSum([2, 7, 11, 15], 9))
print(solutionobject.twoSum([3, 2, 4], 6))
print(solutionobject.twoSum([3, 2, 3], 6))