class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i,num in enumerate(nums):
            
            current_value = target - num

            if current_value in index_map:
                return [index_map[current_value],i]
            index_map[num] = i
 
        
        


