class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #act->act,cat->act
        #key = ''.join(sorted(that string in the arr))
        mapper = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))#cat->act, etc
            mapper[key].append(s)
        return list(mapper.values())