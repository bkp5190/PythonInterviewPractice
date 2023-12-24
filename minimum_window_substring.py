from typing import List

def minWindow(s: str, t: str) -> str:

    # Two hashmaps for the window and string t
    count_t, window = {}, {}

    # Populate the hash map
    for char in t:
        count_t[char] = 1 + count_t.get(char, 0)

    # Have and need variables
    have, need = 0, len(count_t)

    # Result variables
    res, res_len = [-1, -1], float('inf')

    # Left pointer
    left = 0

    # Iterate through the string

    for right in range(len(s)):
        # Set variable for current character
        char = s[right]

        # Update the count in the window hash map
        window[char] = 1 + window.get(char, 0)

        # Check if the chracter is in the t hash map and compare counts
        if char in count_t and window[char] == count_t[char]:
            # Increment the have counter
            have += 1

        # Valid substring encountered
        while have == need:

            # Calculate and update result variables
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            # Decrease the window and update left
            window[s[left]] -= 1
            if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                have -= 1
            left += 1

    l, r = res
    return s[l:r + 1] if res_len != float('inf') else ""

assert minWindow('ADOBECODEBANC', 'ABC') == 'BANC'
assert minWindow('a', 'a') == 'a'
assert minWindow('a', 'aa') == ''
