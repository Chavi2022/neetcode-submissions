class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       #check anagrams:key=tuple(sorted(s))
        d = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            d[key].append(i)
        return list(d.values())