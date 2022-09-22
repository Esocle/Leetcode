class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = []
        res = ''
        for e in strs:
            temp.append(len(e))
        fix_length = min(temp)
        for i in range(fix_length):
            standard = strs[0][i]
            for e in strs:
                if e[i] != standard:
                    return res
            res += standard
        return res