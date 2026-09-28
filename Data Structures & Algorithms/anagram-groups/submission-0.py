class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)

        for s in strs:
            pos = [0] * 26

            for c in s:
                pos[ord(c) - ord('a')] += 1

            groups[tuple(pos)].append(s)

        return list(groups.values())
        
        