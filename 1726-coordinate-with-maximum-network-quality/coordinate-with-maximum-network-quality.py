class Solution:
    def bestCoordinate(self, towers, radius):
        ans = [0, 0]
        best = -1

        for x in range(51):
            for y in range(51):
                quality = 0

                for tx, ty, q in towers:
                    dist = ((x - tx) ** 2 + (y - ty) ** 2) ** 0.5
                    if dist <= radius:
                        quality += int(q / (1 + dist))

                if quality > best:
                    best = quality
                    ans = [x, y]

        return ans