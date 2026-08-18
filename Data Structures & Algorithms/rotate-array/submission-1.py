class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n 
        # If k is larger than the array rotating repeats 
        # if k = 10 and n = 7 then 10 % 7 = 3 
        # rotating 10 times same as rotating 3 times 
        # [1,2,3,4,5,6,7]
        nums.reverse()
        # [7,6,5,4,3,2,1]
        nums[:k] = reversed(nums[:k])
        # First K elements = [5,6,7] [5,6,7,4,3,2,1]
        nums[k:] = reversed(nums[k:])
        # remaining k elements = [5,6,7,1,2,3,4]