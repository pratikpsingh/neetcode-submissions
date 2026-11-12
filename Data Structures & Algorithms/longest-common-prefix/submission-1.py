class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = -1
        flag = False
        first_string = strs[0]
        for i in range(len(first_string)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or first_string[i] != strs[j][i]:
                    return first_string[:common_prefix + 1]
            common_prefix += 1
        return first_string[:common_prefix + 1]