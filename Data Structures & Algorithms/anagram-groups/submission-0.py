class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rs = defaultdict(list)
        for s in strs:
            ss = ''.join(sorted(s))
            rs[ss].append(s)
        return list(rs.values())

        print(s)
