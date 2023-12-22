from typing import List

strs = ["flower", "flow", "flight"]

def longestCommonPrefix(stringList: List[str]):
    prefix = ""
    # Return the longest common prefix between the strings
    # Up to 200 strings each with up to 200 characters
    strs.sort()
    print(strs)
    first, last = strs[0], strs[-1]
    print(f"First: {first}")
    print(f"Last: {last}")
    print(f"{range(min(len(first), len(last)))}")
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return prefix
        prefix += first[i]
    return prefix

output = longestCommonPrefix(strs)


assert output == "fl"
