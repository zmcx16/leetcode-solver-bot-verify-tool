from typing import List

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        x = 0
        y = 0
        visited = set([(0, 0)])
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        d = 0
        for i in distance:
            for _ in range(i):
                x += directions[d][0]
                y += directions[d][1]
                if (x, y) in visited:
                    return True
                visited.add((x, y))
            d = (d + 1) % 4
        return False