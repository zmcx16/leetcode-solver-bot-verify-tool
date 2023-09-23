class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        total_len = word_len * len(words)
        result = []
        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        for i in range(len(s) - total_len + 1):
            seen = {}
            j = 0
            while j < total_len:
                word = s[i + j:i + j + word_len]
                if word in word_freq:
                    if word in seen:
                        seen[word] += 1
                    else:
                        seen[word] = 1
                    if seen[word] > word_freq[word]:
                        break
                else:
                    break
                j += word_len
            if j == total_len:
                result.append(i)
        return result
