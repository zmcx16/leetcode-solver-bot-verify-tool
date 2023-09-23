from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            grouped_anagrams[sorted_word].append(word)
        return list(grouped_anagrams.values())