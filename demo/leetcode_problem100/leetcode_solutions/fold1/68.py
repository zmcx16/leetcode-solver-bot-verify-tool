class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        current_line = []
        current_width = 0
        for word in words:
            if current_width + len(current_line) + len(word) > maxWidth:
                spaces_needed = maxWidth - current_width
                if len(current_line) == 1:
                    line = current_line[0] + ' ' * spaces_needed
                else:
                    spaces_between = spaces_needed // (len(current_line) - 1)
                    extra_spaces = spaces_needed % (len(current_line) - 1)
                    line = ''
                    for i in range(len(current_line) - 1):
                        line += current_line[i] + ' ' * spaces_between
                        if i < extra_spaces:
                            line += ' '
                    line += current_line[-1]
                lines.append(line)
                current_line = []
                current_width = 0
            current_line.append(word)
            current_width += len(word)
        last_line = ' '.join(current_line)
        last_line += ' ' * (maxWidth - len(last_line))
        lines.append(last_line)
        return lines