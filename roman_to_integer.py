# Write a function that returns the roman numeral value given a string input.

class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}

        total = 0
        previous = 0


        for numeral in s:
            current = numerals[numeral]
            if current > previous:
                total += current - 2 * previous
            else:
                total += current
            previous = current

        return total
    
test_numeral_1 = 'III'
test_numeral_2 = 'LVIII'
test_numeral_3 = 'MCMXCIV'

solution = Solution()

print(solution.romanToInt(test_numeral_1))
print(solution.romanToInt(test_numeral_2))
print(solution.romanToInt(test_numeral_3))