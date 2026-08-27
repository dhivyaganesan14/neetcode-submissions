class Solution:
    def trap(self, h: List[int]) -> int:
        total_water_count = 0
        left = 0
        right = len(h)-1
        left_max = 0
        right_max = 0

        while left < right :
            if h[left] <= h[right]:
                # prcoess the left side since right side is already tall 
                if h[left] >= left_max :
                    left_max = h[left]
                else:
                    total_water_count += left_max - h[left]
                left += 1
            
            else : 
                # process the right side since left is already tall 

                if h[right] >= right_max:
                    right_max = h[right]
                else :
                    total_water_count += right_max - h[right]
                right -= 1
            
        return total_water_count


# Time =o(n)
# Space = o(1)

# For each position: water depends on the tallest wall on the left and right.
# Instead of repeatedly searching both sides, track left_max and right_max while using two pointers.

        