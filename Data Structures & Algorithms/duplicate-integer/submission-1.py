class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elementseen = set()
        for i in range(len(nums)):
            if nums[i] in elementseen:
                return True 
            elementseen.add(nums[i])
        return False