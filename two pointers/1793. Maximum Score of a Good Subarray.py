class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        left_pointer = right_pointer = k
        min_value = nums[k]
        max_score = min_value * (right_pointer - left_pointer + 1)

        while left_pointer > 0 or right_pointer < len(nums) - 1:
            check_left = nums[left_pointer - 1] if left_pointer > 0 else 0
            check_right = nums[right_pointer + 1] if right_pointer < len(nums) - 1 else 0

            if check_left >= check_right:
                left_pointer -= 1
                min_value = min(min_value, check_left)
            else: 
                right_pointer += 1
                min_value = min(min_value, check_right)

            max_score = max(max_score, min_value * (right_pointer - left_pointer + 1))

        return max_score
            