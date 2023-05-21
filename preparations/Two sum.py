class Solution(object):
    def twoSum(self, nums, target):
        lst = []
        for i in range(len(nums)):
            if nums[i] + nums[i+1] == target:
                lst.append(nums.index(nums[i]))
                lst.append(nums.index(nums[i+1]))
                return lst

nums = [3,3]
target = 6
n = Solution()
print(n.twoSum(nums,target))