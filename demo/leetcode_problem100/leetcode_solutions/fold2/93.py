def restoreIpAddresses(self, s: str) -> List[str]:
    def backtrack(start: int, parts: List[str], result: List[str]) -> None:
        # Base case: if we have placed 3 dots and the remaining string forms a valid IP address
        if len(parts) == 4 and start == len(s):
            result.append('.'.join(parts))
            return

        # Backtracking
        for i in range(start, min(start + 3, len(s))):
            if s[start] == '0' and i > start:
                break

            num = int(s[start:i+1])
            if num <= 255:
                parts.append(str(num))
                backtrack(i + 1, parts, result)
                parts.pop()

    result = []
    backtrack(0, [], result)
    return result
