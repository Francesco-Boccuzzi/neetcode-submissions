class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = False
        for i in range(len(nums)):
            element = nums.pop()
            if element in nums:
                duplicate = True

        return duplicate