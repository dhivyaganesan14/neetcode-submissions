class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # ( n log n )
        result = [] # o (1)
        for i in range(len(nums)): # o(n)
            #Skip the duplicate values - skip the values while searching 
            if i >0 and nums[i] == nums[i-1]:
                continue 
            p = i+1 
            j = len(nums)-1
            while p < j : #o(n)
                current_sum = nums[i] + nums[p] + nums[j] 
                if current_sum == 0 :
                    result.append([nums[i],nums[p],nums[j]])
                    p += 1
                    j -= 1

                    #Skip the duplicate values 
                    while p<j and nums[p] == nums[p-1]:
                        p += 1

                    #Skip the duplicate values 
                    while p<j and nums[j] == nums[j+1]:
                        j -= 1
                elif current_sum < 0 :
                    p += 1
                else:
                    j -= 1
                
        return result


        # Space = o(1)
        # Time = O(n log n) + o(n2) = o(n2)
