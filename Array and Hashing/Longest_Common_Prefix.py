"""14. Longest Common Prefix
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flogger"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        for j in range(len(prefix)):
            if j == len(s) or prefix[j] != s[j]:
                prefix = prefix[:j]
                break

        if not prefix:
            return ""

    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
