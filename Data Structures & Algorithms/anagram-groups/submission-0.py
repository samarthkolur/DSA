class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for s in strs:
            key = "".join(sorted(list(s)))

            if key in dict.keys():
                dict[key].append(s)
                continue
            
            dict[key] = [s]
        
        return list(dict.values())
            