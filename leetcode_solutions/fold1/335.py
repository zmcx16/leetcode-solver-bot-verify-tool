class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        visited = set()
        x, y = 0, 0
        direction = 0
        visited.add((x,y))
        for d in distance:
            if direction == 0:
                for _ in range(d):
                    y += 1
                    if (x, y) in visited:
                        return True
                    visited.add((x, y))
                direction = 1
            elif direction == 1:
                for _ in range(d):
                    x -= 1
                    if (x, y) in visited:
                        return True
                    visited.add((x, y))
                direction = 2
            elif direction == 2:
                for _ in range(d):
                    y -= 1
                    if (x, y) in visited:
                        return True
                    visited.add((x, y))
                direction = 3
            else:
                for _ in range(d):
                    x += 1
                    if (x, y) in visited:
                        return True
                    visited.add((x, y))
                direction = 0
        return False