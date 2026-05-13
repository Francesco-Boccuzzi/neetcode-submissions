class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for j in range(len(nums)):
            goal = target - nums[j]
            if goal in hashMap:
                return [hashMap[goal], j]
            else:
                hashMap[nums[j]] = j

