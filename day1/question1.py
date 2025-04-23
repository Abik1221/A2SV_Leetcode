# There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

# The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

# You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

# You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

# Return the minimum capability of the robber out of all the possible ways to steal at least k houses.


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_steal_k_houses(capability):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 2 
                else:
                    i += 1
            return count >= k
        
        left, right = min(nums), max(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            if can_steal_k_houses(mid):
                right = mid
            else:
                left = mid + 1
                
        return left    