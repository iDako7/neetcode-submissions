class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        # abc and acb
        # key is sorted string, value is the a list contains all the example

        # for s in str:
            # sort s
            # res[k].append(s)
        
        # res = [for val in res.value()]

        count = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            count[key].append(s)
        
        res = list(count.values())
        return res
