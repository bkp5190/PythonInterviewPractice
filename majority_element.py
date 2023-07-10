# Write a function that returns the majority element which appears more than n/2 times.


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Intuitive with dictionary
        def intuitive_approach(nums: List[int]) -> int:
            d = {}

            for i in nums:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1

            return max(d, key=d.get)

            # Moore's Voting Algorithm O(n) time, O(1) space
        def moores_voting_algorithm(nums: List[int]) -> int:
            counter = 0
            candidate = 0

            for num in nums:
                if counter == 0:
                    candidate = num

                if num == candidate:
                    counter += 1
                else:
                    counter -= 1

            return candidate
        # return intuitiveApproach(nums)
        return moores_voting_algorithm(nums)


solution = Solution()
print(solution.majorityElement([1, 2, 2, 2, 3]))
print(solution.majorityElement([2, 5, 6, 2, 3, 4, 4, 4, 3]))
print(solution.majorityElement([3, 2, 3]))
