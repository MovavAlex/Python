class Solution(object):
    def twoSum(self, nums, target):
        lst = []
        for i in range(len(nums)):
            if target - nums[i] in nums:
                lst.append(nums.index(nums[i]))
                x = target - nums[i]
                lst.append(nums.index(x))
                return lst
            elif nums[i] == nums[i+1]:
                lst.append(nums.index(nums[i]))
                lst.append(nums.index(nums[i+1]))


nums = [3,3]
target = 6
n = Solution()
print(n.twoSum(nums,target))