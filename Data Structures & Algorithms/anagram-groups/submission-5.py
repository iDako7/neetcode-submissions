class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: sorted string, value: matched item --> list, return the value into a list
        # enhancement: use ASCII to replace sort
        from collections import defaultdict
        group = defaultdict(list)

        for s in strs:
            # count the frequency of each character in this string
            # use count as key to match different strings, replace sort
            # time complexity improved from  O(n · k log k) to  O(n · k)
            count = [0] * 26
            for c in s:
                # syntax error: count[ord[c]-ord['a']] += 1
                count[ord(c) - ord('a')] += 1
            
            # syntax error: group(tuple(count)).append(s)
            group[tuple(count)].append(s)
        
        return list(group.values())