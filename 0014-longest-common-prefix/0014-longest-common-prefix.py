class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for strs in strs[1:]:
            while not strs.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix