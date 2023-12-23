def lengthOfLongestSubstring(s: str) -> int:
    # Create an encoutered set to track duplicates
    encountered = set()

    # Initialize the left pointer and the max length variables
    l = max_length = 0

    # Iterate through the array with the right pointer
    for r in range(len(s)):
        # While the right pointer has a value already encountered
        while s[r] in encountered:
            # Remove the left most value from the hash set
            encountered.remove(s[l])
            # Increment the left pointer
            l += 1
        # Add the right most value to the hash set
        encountered.add(s[r])
        # Compute the max length with the pointers
        max_length = max(max_length, r - l + 1)

    # Return the final max length
    return max_length

assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3
