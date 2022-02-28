from typing import List

class Solution:

    # Brute Force solution
    # ----------------------------------------------------
    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        for x in range(length):
            for y in range(x+1,length):
                if nums[x]+nums[y] == target:
                    return [x,y]
        return []

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum_brute_force([3, 2, 4], 6))