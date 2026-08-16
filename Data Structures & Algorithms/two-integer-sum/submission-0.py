class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i,num in enumerate(nums):
            index_map[num] = i 
        
        for i in range(len(nums)):
            current_value = target - nums[i]

            if current_value in index_map:
                if i != index_map[current_value]:
                    return[i,index_map[current_value]]


Time Complexity : O(n) + O(n) = O(2n) = O(n) 
one for constructing map 
one for iteration 
# 2 passes 
Space : o(n) 
for hashmap
