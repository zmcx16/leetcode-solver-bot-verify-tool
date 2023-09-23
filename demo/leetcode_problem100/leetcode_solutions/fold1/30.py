class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        words_len = len(words) * word_len
        result = []
        count = Counter(words)
        for i in range(len(s) - words_len + 1):
            curr_count = Counter()
            j = 0
            while j < words_len:
                word = s[i + j:i + j + word_len]
                if word not in count or curr_count[word] == count[word]:
                    break
                curr_count[word] += 1
                j += word_len
            if j == words_len:
                result.append(i)
        return result
