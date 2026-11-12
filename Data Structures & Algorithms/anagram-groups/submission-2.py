class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)

        # for s in strs:
        #     count = [0] * 26

        #     for c in s:
        #         count[ord(c) - ord('a')] += 1

        #     res[tuple(count)].append(s)
        
        # return [res[key] for key in res]

        # Method 2
        res = {}

        for s in strs:
            sort_s = str(sorted(s))
            if sort_s in res:
                res[sort_s].append(s)
            else:
                res[sort_s] = [s]
        return [list(x) for x in res.values()]