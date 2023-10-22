class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_vol = -1
        left_border_idx, right_border_idx = 0, len(height)-1

        while left_border_idx != right_border_idx:
            current_vol = (right_border_idx - left_border_idx) * min(height[left_border_idx], height[right_border_idx])
            if max_vol < current_vol:
                max_vol = current_vol
            if height[left_border_idx] >= height[right_border_idx]:
                right_border_idx -= 1
                continue
            left_border_idx += 1
        return max_vol