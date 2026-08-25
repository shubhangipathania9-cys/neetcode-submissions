class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []

        def backtrack():
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return

            for num in nums:
                if num in permutation:
                    continue

                permutation.append(num)
                backtrack()
                permutation.pop()

        backtrack()
        return result
        