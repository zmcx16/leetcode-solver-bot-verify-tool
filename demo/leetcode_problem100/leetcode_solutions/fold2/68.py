class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(current_line) + len(word) > maxWidth:
                spaces_needed = maxWidth - current_length
                gaps = len(current_line) - 1
                
                if gaps == 0:
                    line = current_line[0] + ' ' * spaces_needed
                else:
                    spaces_per_gap = spaces_needed // gaps
                    extra_spaces = spaces_needed % gaps
                    
                    line = current_line[0]
                    for i in range(1, len(current_line)):
                        line += ' ' * (spaces_per_gap + 1)
                        if i <= extra_spaces:
                            line += ' '
                        line += current_line[i]
                
                lines.append(line)
                current_line = []
                current_length = 0
            
            current_line.append(word)
            current_length += len(word)
        
        last_line = ' '.join(current_line)
        last_line += ' ' * (maxWidth - len(last_line))
        lines.append(last_line)
        
        return lines