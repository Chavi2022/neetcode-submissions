class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key = ''.join(sorted(i))
        anagramMap = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            anagramMap[key].append(i)
        return list(anagramMap.values())