# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def min_subarrays_required(max_sum_allowed: int) -> (bool, int):
            current_sum = 0
            splits_required = 1  # Start with one subarray
            max_subarray_sum = 0  # To track the maximum sum among subarrays

            for element in nums:
                next_sum = current_sum + element

                if next_sum <= max_sum_allowed:
                    # Include the element in the current subarray
                    current_sum = next_sum
                else:
                    # Start a new subarray
                    max_subarray_sum = max(max_subarray_sum, current_sum)
                    current_sum = element
                    splits_required += 1  # Increment the number of subarrays

                    if splits_required > m:
                        # Early exit if splits exceed m
                        return False, None

            # Update max_subarray_sum for the last subarray
            max_subarray_sum = max(max_subarray_sum, current_sum)
            return True, max_subarray_sum

        left = max(nums)
        right = sum(nums)
        minimum_largest_split_sum = right  # Initialize with the maximum possible sum
        step = 0  # Step counter

        while left <= right:
            step += 1

            if step == 1:
                # Initial estimate for max_sum_allowed
                max_sum_allowed = (left + right) // m
            else:
                max_sum_allowed = (left + right) // 2

            can_be_done, max_subarray_sum = min_subarrays_required(max_sum_allowed)

            if can_be_done:
                # Update minimum_largest_split_sum and search left half
                minimum_largest_split_sum = min(minimum_largest_split_sum, max_subarray_sum)
                right = max_subarray_sum - 1
            else:
                # Search right half
                left = max_sum_allowed + 1

        return minimum_largest_split_sum