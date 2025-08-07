class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        1. Sort the array.
        2. Fix the first element and use a two-pointer approach to find the other two.
        3. Duplicates are taken care of because of unique set.
        '''
        if len(nums) < 3:
            return []
        nums.sort()
        result = []
        unique = set()
        for i in range(0,len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    unique.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        for item in unique:
                result.append(item)
        return result
        
        