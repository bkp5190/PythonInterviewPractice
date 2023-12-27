def longestPalindrome(s: str) -> str:
    # Sliding window problem
    left = 0
    max_length = 0

    for right in range(len(s)):
        # check if the substring is a palindrome
        while isPalindrome(s[left:right]):
            # Update the max_length
            max_length = right - left + 1

        # Decrease the window
        left += 1

    return max_length

def isPalindrome(s: str) -> bool:
    # Two pointer
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


assert longestPalindrome('babad') == 'bab' or 'aba'
assert longestPalindrome('cbbd') == 'bb'
