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

    # With Hash table
    # ----------------------------------------------------
    # Hash table formate
    # num : index positions

    def twoSum_hashTable_trycatch(self, nums: List[int], target: int) -> List[int]:
        hash_table={}
        nums:int
        index:int
        remaining:int
        for index, num in enumerate(nums):
            remaining=target-num;
            try:
                hash_table[remaining];
                return [hash_table[remaining],index];
            except KeyError:
                hash_table[num]=index;
    
    def twoSum_hashTable(self, nums: List[int], target: int) -> List[int]:
        hash_table={}
        for index, num in enumerate(nums):
            remaining=target-num
            if remaining in hash_table.keys():
                return [hash_table[remaining],index]
                
            hash_table[num]=index
        return []
        

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum_hashTable([3, 2, 4], 6))