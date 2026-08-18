class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        #[1,2,3,4,5,6,7]
        k = k % n #3 % 7 = 3 
        def reverse (left,right):
            while left<right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        
        reverse (0,n-1) #[7,6,5,4,3,2,1]
        reverse (0,k-1) #[5,6,7,4,3,2,1]
        reverse (k,n-1) #[5,6,7,1,2,3,4]

# Time = O(n)
# Space = O(1)

# Slicing creates new lists - so o(n) space 