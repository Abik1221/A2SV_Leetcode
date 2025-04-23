# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.




class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        def find_target(left, right, target, is_upside):
            while left <= right:
                mid = (left + right) // 2
                mid_val = mountain_arr.get(mid)

                if mid_val == target:
                    return mid
                
                if is_upside:
                    if target > mid_val:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if target > mid_val:
                        right = mid - 1
                    else:
                        left = mid + 1

            return -1

        def find_peak():
            nonlocal length

            left, right = 0, length - 1

            while left < right:
                mid = (left + right) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            
            return left

        peak_index = find_peak()


        result = find_target(0, peak_index, target, True)
        if result != -1:
            return result
        
        return find_target(peak_index + 1, length - 1, target, False)        