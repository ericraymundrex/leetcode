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


    def twoSum_hashTable(self, nums: List[int], target: int) -> List[int]:
        hash_table={}
        for index, num in enumerate(nums):
            another=target-num
            try:
                hash_table[another]
                return [hash_table[another],index]
            except KeyError:
                hash_table[num]=index

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum_hashTable([3, 2, 4], 6))