class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []

        def backtrack(i, total):
            if total == target:
                result.append(combination[:])
                return

            if i >= len(nums) or total > target:
                return

            combination.append(nums[i])
            backtrack(i, total + nums[i])

            combination.pop()
            backtrack(i + 1, total)

        backtrack(0, 0)
        return result