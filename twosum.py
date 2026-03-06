class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i


nums = list(map(int, input().split()))
target = int(input())

obj = Solution()
print(obj.twoSum(nums, target))